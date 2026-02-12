from datetime import datetime
from django.utils import timezone

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from task.models import Task, TaskComp
from task.chek import is_task_completed as exist_chek
@login_required(login_url='user:login')
def dashboard(request):

    task=Task.objects.filter(user=request.user,is_active=True,is_deleted=False)
    complete_task=[]
    pending_task=[]

    for comp_t in task:
        flag =exist_chek(comp_t.id,comp_t.task_type)
        task = Task.objects.get(id=comp_t.id)

        if flag and task.created_at <= timezone.now():

            if comp_t.task_type == "Once" :
                continue
            else:
                complete_task.append(comp_t)
        elif flag is False and task.created_at <= timezone.now():
            pending_task.append(comp_t)
    totel_complete_task=complete_task.__len__()
    totel_task=complete_task.__len__()+pending_task.__len__()
    return render(request, 'dashboard/dashboard.html',{"complete_task":complete_task,"pending_task":pending_task,"totel_complete_task":totel_complete_task,"totel_task":totel_task})


def rankin(request):
    return render(request,"dashboard/ranking.html")
