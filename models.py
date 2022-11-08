from django.db import models

# Create your models here.
class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)

class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    DateOfJoining= models.DateField()
    EmployeeDepartment = models.ForeignKey(Department, on_delete=models.CASCADE)
    PhotoFileName = models.CharField(max_length=100)
