from django.db import models
from Data.models.Employee import Employee
from rest_framework import serializers


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Employee
        fields = ('empname', 'Designation','mobile','reporting') 