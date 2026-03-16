from django.db import models

# Create your models here.

class employee(models.Model):
    employee_id = models.CharField(max_length=25)
    employee_name = models.CharField(max_length=40)
    employee_email = models.EmailField()
    employee_contanct = models.IntegerField()
    
    def __str__(self):
        return self.employee_name
