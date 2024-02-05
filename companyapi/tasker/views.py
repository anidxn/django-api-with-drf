from rest_framework.decorators import api_view
from rest_framework.response import Response
# ------- serializer -----------
from .serializers import TaskSerializer


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
        pdata = request.data        # get the request data
        serializer = TaskSerializer(data = pdata)   # initialize an Serializer object with request data

        # validate serializer data i.e. if user supplied less or excessive data fields
        if serializer.is_valid():
            print(serializer.data)

            return Response({
                "status" : True,
                "message": "valid data",
                'data' : serializer.data
            })
        else:
            return Response({
                "status" : False,
                "message": "In valid data",
                'data' : serializer.errors
            })
    
    except Exception as e:
        return Response({
            "status" : False,
            "message": "Something went wrong",
        })