from django.contrib import admin
from .models import UserInfoModel,TaskModel

# Register your models here.

admin.site.register(UserInfoModel)
admin.site.register(TaskModel) 
