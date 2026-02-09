from django.contrib import admin
from django.urls import path ,include
from . import views
app_name="task"
urlpatterns = [

    path('task/',views.task,name="task"),

]