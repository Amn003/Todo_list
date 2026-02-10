from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout,login
from .models import profile
import uuid
# Create your views here.
def loginc(request):
    if request.user.is_authenticated:
        return redirect("dashboard:dashboard")
    return redirect("user:login")

def login_user(request):
    if request.user.is_authenticated:
        return redirect("dashboard:dashboard")
    
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            user=User.objects.get(email=email,)
        except User.DoesNotExist as err:
            messages.error(request,err)
            redirect("user:login")
        user=authenticate(
            request,
            username=user.username,
            password=password,
        )   

        if user is not None:
            login(request,user)
            print(user)

            return redirect('dashboard:dashboard')
        messages.error(request,"Invalid email or password")
        return render(request, 'user/login.html')


    return render(request,"user/login.html")


def register(request):
    if request.method == "POST":

        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        password=request.POST.get("password")
        repeat_password=request.POST.get("repeat_password")
        occupation=request.POST.get("occupation")



        if User.objects.filter(email=email).exists():
            messages.error(request,"This mail Id Already exist")

            return redirect("user:register")
        username = first_name+f"{uuid.uuid4().hex[:8]}"
        
        try :
            while User.objects.filter(username=username).exists():
                username = first_name+f"{uuid.uuid4().hex[:8]}"
            print(f"\n\n {username}")
            user=User.objects.create_user(
                username = username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name, 
                )
            profile.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                occupation=occupation
                )
            messages.success(request,f"You are registered as {first_name}")
            return redirect('user:login')
        except Exception as err:
            messages.error(request,err)
            return redirect("user:register")
    return render(request,"user/register.html")



def logout_user(request):

    logout(request)
    return redirect("user:login")