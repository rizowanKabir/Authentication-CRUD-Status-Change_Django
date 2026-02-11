from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserInfoModel(AbstractUser):
    USER_TYPE = [
        ('User', 'User'),
        ('Admin', 'Admin')
    ]
    full_name = models.CharField(max_length=100, null=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=150, null=True)

    def __str__(self):
        return self.username 
    
class TaskModel(models.Model):
    STATUS = [
        ('NotStarted','NotStarted'),
        ('InProgress', 'InProgress'),
        ('Completed', 'Completed')
    ]
    task_name = models.CharField(max_length=100, null=True) 
    task_description = models.TextField(null=True)  
    task_status = models.CharField(choices=STATUS, max_length=20, null=True)
    deadline = models.DateField(null=True)
    created_by = models.ForeignKey(UserInfoModel, on_delete=models.CASCADE, related_name='task_user',null=True)

    def __str__(self):
        return self.task_name 

