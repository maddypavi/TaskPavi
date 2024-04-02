from django.db import models


class Manager(models.Model):
    name = models.CharField(max_length=255,unique=True)
    age = models.IntegerField()
    mobile=models.IntegerField()
    class Meta:
        db_table = 'Manager'

    def __str__(self):
        return self.name