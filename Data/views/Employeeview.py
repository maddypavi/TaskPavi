from rest_framework import viewsets 

# import local data 
from Data.serializers.Employeeserializers import EmployeeSerializers
from Data.models.Employee import Employee
  
# create a viewset 
class EmployeeViewSet(viewsets.ModelViewSet): 
    # define queryset 
    queryset = Employee.objects.all() 
      
    # specify serializer to be used 
    serializer_class = EmployeeSerializers 