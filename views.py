from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,'home.html',{})




def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        if password1 != password2:
            return HttpResponse("Password is incorrect")
        try:
            if User.objects.get(username=username):
                messages.warning(request,'Username has already been taken ')
                return redirect('signup')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,'Email has already been taken')
                return redirect('signup')
        except:
            pass
        myuser=User.objects.create_user(username,email,password1)
        myuser.save() 
    return render(request,'signup.html',{})



def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        email=request.POST.get('email')
        myuser=authenticate(username=username,password=pass1,email=email)
        if myuser is not None:
            login(myuser)
            messages.success(request,'login Successfully')
            return redirect('home')
        else:
            messages.error(request,'create a new account')
            return redirect(request,'login')        
    return render(request,'login.html',{})




def order_form(request):
    return render(request,'order_form.html',{})






#def home(request):
 #   return render(request,'home.html',{})
