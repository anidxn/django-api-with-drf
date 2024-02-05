#create serializers
from rest_framework import serializers
from api.models import Company, Employee

# Company Serializer
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # make read-only fields (such as PKey) visible in API result
    company_id = serializers.ReadOnlyField() 
    #*** variable name should be same as the table column name – use dbbrowser

    class Meta:
        model = Company
        fields = "__all__" # I want to include all fields of Company Model, if I want to hide some column then give ['col1', 'col2',...]


# Employee serializer
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField() 

    class Meta:
        model = Employee
        fields = "__all__"
