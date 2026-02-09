from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User



@login_required(login_url='user:login')
def dashboard(request):
    messages.success(request, f"Login Sucessfully as {request.user.first_name}")
    return render(request, 'dashboard/dashboard.html')
