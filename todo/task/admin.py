from django.contrib import admin
from .models import task,TaskComp
# Register your models here.

admin.site.register(task)
admin.site.register(TaskComp)