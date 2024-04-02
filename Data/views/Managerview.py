from rest_framework import viewsets 
  
# import local data 
from Data.serializers.Managerserializers import ManagerSerializers
from Data.models.Manager import Manager
  
# create a viewset 
class ManagerViewSet(viewsets.ModelViewSet): 
    # define queryset 
    queryset = Manager.objects.all() 
      
    # specify serializer to be used 
    serializer_class = ManagerSerializers 