from django.db import models
from Data.models.Manager import Manager
from rest_framework import serializers


class ManagerSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Manager
        fields = ('name', 'age','mobile') 