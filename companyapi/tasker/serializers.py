from rest_framework import serializers
from .models import Task, TimingTask
# regular expression for validation
import re

from django.template.defaultfilters import slugify

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    uid = serializers.ReadOnlyField()    #*** variable name should be same as the table column name – use dbbrowser
    slug = serializers.SerializerMethodField()  #intialize a slug with defined function

    class Meta:
        model = Task
        # fields = "__all__"   # To restric use ['', '', '', 'slug']
        exclude = ['created_at', 'updated_at']
    
    def get_slug(self, obj):
        return slugify(obj.task_title)


    def validate(self, validated_data):
        # validate that title should not have any special symbol
        if validated_data.get('task_title'):
            # grab title from received data
            title = validated_data['task_title']

            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
     
            # Pass the string in search method of regex object.    
            if not (regex.search(title) == None):
                raise serializers.ValidationError('Title can not contain special characters')
        
        # validate description for length - This works perfectly, we can also validate a specific field like below
        # if  validated_data.get('task_desc'):
        #     desc = validated_data['task_desc']

        #     if len(desc) < 3:
        #         raise serializers.ValidationError('Too small description')
            
        # if all ok above then come here & return the received data 
        return validated_data
    
    # -------- to validate a specific column ---------
    def validate_task_desc(self, data):     # validate_<column_name>
        if data:
            desc = data

            if len(desc) < 3:
                raise serializers.ValidationError('Too small description')
        
        return data
    

# ============================================
#       
# ============================================
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimingTask
        exclude = ['created_at', 'updated_at']