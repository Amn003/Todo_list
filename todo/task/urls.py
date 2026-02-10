from django.contrib import admin
from django.urls import path ,include
from . import views
app_name="task"
urlpatterns = [

    path('task/',views.task,name="task"),
    path('creat-task/',views.creat_task,name="creat-task"),
    path('complete/<int:task_id>/',views.complete_task,name="complete"),
    path('pause/<int:task_id>/',views.pause_task,name="pause"),
    path('delete/<int:task_id>/',views.delete_task,name="delete"),

]