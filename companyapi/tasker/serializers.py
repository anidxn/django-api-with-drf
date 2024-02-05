from rest_framework import serializers
from .models import Task

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    company_id = serializers.ReadOnlyField()    #*** variable name should be same as the table column name – use dbbrowser

    class Meta:
        model = Task
        fields = "__all__"   # To restric use ['', '', '', ...]