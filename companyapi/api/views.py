from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer

# Create your view class extending viewsets.ModelViewSet; this viewset default `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()` and `list()` actions.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    # use the following serializer class for serializing the resultset
    serializer_class = CompanySerializer

    # for custom URLs=======================>>>>>>>>>
    # companies/{company_id}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk = None):
        # print("get employees of ", pk, "company")
        try:
            #-- get the company base on the id (here it is pkey)..Qs. wht if the search criteria is not pkey??
            comp = Company.objects.get(pk = pk)
            # == get the list of employees corresponding to that company object
            emplist = Employee.objects.filter(company = comp) # object matching; not just any particular field
            # serialize the list to be displayed
            emps_serializer = EmployeeSerializer(emplist, many=True, context = {'request': request})
            """
                many = True --> lots of data
            """
            # == return the response
            return Response(emps_serializer.data) # send API response in JSON format
        except Exception as e:
            print(e)  # displays message in console
            return Response({'message' : 'Company data might not exist'})  # send API response in JSON format


# employee viewSet
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
