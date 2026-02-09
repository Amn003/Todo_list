from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from .models import Task, TaskComp
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
    messages.success(request, f"inside the complete_task")
    return redirect("dashboard:dashboard")