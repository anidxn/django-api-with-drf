#--------------- decorator ----------------
from rest_framework.decorators import api_view
from rest_framework.response import Response
# ------- serializer -----------
from .serializers import TaskSerializer
from .models import Task
# ---------------- APIView ------------------
from rest_framework.views import APIView

# ------------ for product class based view & search on that------------
from .models import Product
from .serializers import ProductSerializer

from rest_framework import generics, filters
# ---- for custom serach filter ---
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


@api_view()     # by default allow GET only
def get_name(request):
    """
    return Response({
        "status" : 200,
        "message": "Hello, world!"
        })
    """
    """
    person = {'name': 'Ani', 'age' : 29}
    return Response(person)
    """

    task_list = Task.objects.all()
    serializer = TaskSerializer(task_list, many = True)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'PATCH'])
def home(request):

    if request.method == 'GET':
        return Response({
        "status" : 200,
        "message": "DRF Called",
        "method_called" : "U called GET"
        })
    elif request.method == 'POST':
        return Response({
        "status" : 200,
        "message": "DRF Called",
        "method_called" : "U called POST"
        })
    elif request.method == 'PATCH':
        return Response({
        "status" : 200,
        "message": "DRF Called",
        "method_called" : "U called PATCH"
        })
    else:
        return Response({
        "status" : 200,
        "message": "DRF Called",
        "method_called" : "U called an Invalid method"
        })

# ---------------------Store a task by POST ---------------------
@api_view(['POST'])
def post_task(request):
    try:
        post_data = request.data        # get the request data
        serializer = TaskSerializer(data = post_data)   # initialize an Serializer object with request data, i. serializes data ii. can be used to validate data format

        # validate serializer data i.e. if user supplied less or excessive data fields as specified in the Serializer(here it contains __all__ fields of the Model)
        if serializer.is_valid():
            serializer.save()       # save data to db
            print("Data = ", serializer.data)

            return Response({
                "status" : True,
                "message": "Task created successfully",
                'data' : serializer.data
            })
        else:
            return Response({
                "status" : False,
                "message": "Invalid data",
                'data' : serializer.errors
            })
    
    except Exception as e:
        return Response({
            "status" : False,
            "message": "Something went wrong",
        })

#----------------- get All data ----------------------------
# CALL : GET: http://localhost:8085/api/tasker/gettask
#---------------------------------------------------------

@api_view(['GET'])
def get_task(request):
    task_list = Task.objects.all()
    serializer = TaskSerializer(task_list, many = True)  # many = True --> bcz of many record objects are populated

    return Response({
            "status" : True,
            "message": "Record fetched",
            "Data" : serializer.data
        })

# ------------- GET a single record based on Okey = Uid-----------
# CALL : http://localhost:8085/api/tasker/task-detail/c21dd2d2-f7bf-4abc-96d5-d45d98957b27/
# ------------------------------------------------------------------------------------------

@api_view(['GET'])
def task_detail(request, pk):
    sel_task = Task.objects.get(uid=pk)
    serializer = TaskSerializer(sel_task, many = False)  # many = False --> only 1 object fetched

    return Response({
            "status" : True,
            "message": "Record fetched with the given id",
            "Data" : serializer.data
        })

# ----------- Update ALL fields (PUT)------------------
# CALL: http://localhost:8085/api/tasker/update_task/
# ------------------------------------------------------
@api_view(['PUT'])
def put_task(request):     # here UID is passed as a body parameter (json data), rather than a fixed id in URL
    try:
        post_data = request.data
        if not post_data.get('uid'):   # data MUST contain the primary key
            return Response({
                "status" : False,
                "message": "UID is required",
            })
        
        obj = Task.objects.get(uid = post_data.get('uid'))   # get the object ref which will be updated with new data
        serializer = TaskSerializer(obj, data = post_data)  # destination, Source, Update mode =>partial = False => update all fields

        # ------------ same as post ---------
        if serializer.is_valid():
            serializer.save()

            return Response({
                "status" : True,
                "message": "Task updated successfully",
                'data' : serializer.data
            })
        else:
            return Response({
                "status" : False,
                "message": "Invalid data",
                'data' : serializer.errors
            })
    
    except Exception as e:
        return Response({
            "status" : False,
            "message": "Something went wrong",
        })


# ----------- Update some fields ----------
@api_view(['PATCH'])
def patch_task(request):        # here UID is passed as a body parameter (json data), rather than a fixed id in URL
    try:
        post_data = request.data
        if not post_data.get('uid'):   # data MUST contain the primary key
            return Response({
                "status" : False,
                "message": "UID is required",
            })
        
        obj = Task.objects.get(uid = post_data.get('uid'))   # get the object ref which will be updated with new data
        serializer = TaskSerializer(obj, data = post_data, partial = True)  # destination, Source, Update mode = partial for PATCH

        # ------------ same as post ---------
        if serializer.is_valid():
            serializer.save()

            return Response({
                "status" : True,
                "message": "Task updated successfully",
                'data' : serializer.data
            })
        else:
            return Response({
                "status" : False,
                "message": "Invalid data",
                'data' : serializer.errors
            })
    
    except Exception as e:
        return Response({
            "status" : False,
            "message": "Something went wrong",
        })
    
# ----------- Delete a task------------------
# CALL: http://localhost:8085/api/tasker/task-delete/301ea7f3-098c-4cd3-9c06-393be678e42f/
# ------------------------------------------------------
@api_view(['DELETE'])
def del_task(request, pk):
    sel_task = Task.objects.get(uid=pk)
    sel_task.delete()

    return Response({
            "status" : True,
            "message": "Record deleted",
        })



# =======================================================================================
#   Issue with prev approach: define all methods individually + keep separate URLs for calling them
#   sol: Define a class vased view inheritted from APIView
#   APIView already has 5 function - GET, POST, PUT, PATCH, DELETE, u just need to override them
# =======================================================================================
class TaskView(APIView):
    def get(self, request):
        return Response({
                "status" : 200,
                "message": "DRF Called",
                "method_called" : "U called GET"
            })

    def post(self, request):
        return Response({
                "status" : 200,
                "message": "DRF Called",
                "method_called" : "U called POST"
            })
    
    def patch(self, request):
        return Response({
                "status" : 200,
                "message": "DRF Called",
                "method_called" : "U called PATCH"
            })
    
    def put(self, request):
        return Response({
                "status" : 200,
                "message": "DRF Called",
                "method_called" : "U called PUT"
            })
    
    def delete(self, request):
        return Response({
                "status" : 200,
                "message": "DRF Called",
                "method_called" : "U called DELETE"
            })
    

# SEraching a product using API --> select * from table where pname='...' or description = '....'
# ---------------------------------------------------------------------------------------------------
class ProductSearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #filter_backends = [filters.SearchFilter]  #--> Default style
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'description']
    # filterset_fields = ['price']   --> ommit if custom filter class is used
    filterset_class = ProductFilter

"""
http://localhost:8085/api/tasker/products/?search=laptop

http://localhost:8085/api/tasker/products/?price=80000

http://localhost:8085/api/tasker/products/?search=laptop&price=80000

http://localhost:8085/api/tasker/products/?price__gte=80000

http://localhost:8085/api/tasker/products/?price__lte=80000

http://localhost:8085/api/tasker/products/?price__lt=80000

"""

#-------------------------------------------------------------
#               SEARCH by Date Range
#-------------------------------------------------------------
class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            queryset = queryset.filter(updated_at__range=[start_date, end_date])
        return queryset
    

"""
http://localhost:8085/api/tasker/taskbydate/?start_date=2023-01-01&end_date=2023-12-31
"""

    