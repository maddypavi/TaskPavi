from django.db import models
from Data.models.Manager import Manager


class Employee(models.Model):
    empname = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    mobile = models.IntegerField()
    reporting = models.ForeignKey(Manager, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Employee'

    def __str__(self):
        return self.empname