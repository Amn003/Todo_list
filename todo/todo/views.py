from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import render


# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard:dashboard")
    
    return render(request,"todo/home.html")