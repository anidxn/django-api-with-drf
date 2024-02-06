#--------------- decorator ----------------
from rest_framework.decorators import api_view
from rest_framework.response import Response
# ------- serializer -----------
from .serializers import TaskSerializer
from .models import Task
# ---------------- APIView ------------------
from rest_framework.views import APIView


@api_view()     # by default allow GET only
def get_name(request):
    return Response({
        "status" : 200,
        "message": "Hello, world!"
        })

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

# ------------------------------------------
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

#----------------- get data -------------
@api_view(['GET'])
def get_task(request):
    task_list = Task.objects.all()
    serializer = TaskSerializer(task_list, many = True)  # many = True --> bcz of many record objects are populated

    return Response({
            "status" : True,
            "message": "Record fetched",
            "Data" : serializer.data
        })

@api_view(['PATCH'])
def patch_task(request):
    try:
        post_data = request.data
        if not post_data.get('uid'):   # data MUST contain the primary key
            return Response({
                "status" : False,
                "message": "UID is required",
            })
        
        obj = Task.objects.get(uid = post_data.get('uid'))   # get the object ref which will be updated with new data
        serializer = TaskSerializer(obj, data = post_data, partial = True)  # destination, Source, Update mode

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