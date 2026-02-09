from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render

# Create your views here.

@login_required(login_url="urls:login")
def task(request):
    user=request.user

    return render(request,"task/dashboard.html")

