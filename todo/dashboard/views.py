from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from task.models import Task, TaskComp


@login_required(login_url='user:login')
def dashboard(request):
    messages.success(request, f"Login Sucessfully as {request.user.first_name}")

    task=Task.objects.filter(user=request.user,is_active=True,is_deleted=False)
    print(Task.objects.all())
    return render(request, 'dashboard/dashboard.html',{"task":task})



