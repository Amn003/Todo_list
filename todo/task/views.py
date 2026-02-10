from django.shortcuts import get_object_or_404, render ,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from .models import Task, TaskComp
from .chek import is_task_completed as exist_chek
from datetime import datetime
# Create your views here.

@login_required(login_url="urls:login")
def task(request):
    user=request.user

    return render(request,"task/dashboard.html")


@login_required(login_url='user:login')
def creat_task(request):

    messages.success(request, f"In Creat Task {request.user.first_name}")

    if request.method=="POST":
        titel=request.POST.get("title")
        description=request.POST.get("description")
        task_type=request.POST.get("task_type")
        due_date=request.POST.get("due_date")

        Task.objects.create(
            user=request.user,
            title=titel,
            description=description,

            task_type=task_type,
            created_at=due_date,
        )
        messages.success(request, f"Your task Get Created")
        return redirect("dashboard:dashboard")
    return redirect("dashboard:dashboard")


def complete_task(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    flag=exist_chek(task_id,task.task_type)
    print(f"the flag is {flag}")
    print(task.task_type)
    if flag is False:
        TaskComp.objects.create(task=task,complete_on=datetime.now())
    
    else:
        messages.error(request,"This task is already completed")
        task1=TaskComp.objects.get(task=task)
        print(f" the task is {task1}")
        return redirect("dashboard:dashboard")
    
    messages.success(request, f"inside the complete_task")
    return redirect("dashboard:dashboard")



@login_required(login_url="user:login")
def pause_task(request,task_id):
    try:
        task = get_object_or_404(Task, id=task_id)
        task.is_active=False
        task.save()
        messages.success(request,f"Task {task.title} paused successfully")
    except Task.DoesNotExist:
        messages.error(request,"Task does not exist")
        return redirect("dashboard:dashboard")
    


@login_required(login_url="user:login")
def delete_task(request,task_id):
    try:
        task = get_object_or_404(Task, id=task_id)
        task.is_deleted=True
        task.save()
        messages.success(request,f"Task {task.title} deleted successfully")
    except Task.DoesNotExist:
        messages.error(request,"Task does not exist")
        return redirect("dashboard:dashboard")

