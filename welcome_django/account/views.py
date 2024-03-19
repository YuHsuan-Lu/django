from django.contrib.auth import authenticate,login as auth_login
from django.shortcuts import render,redirect
from .models import User
# Create your views here.
def login(request):
    if request.method=="POST":
        email = request.POST.get('email','')
        password1 = request.POST.get('password1','')
        if email and password1:
            user = authenticate(request,email=email,password=password1)
            if user is not None:
                auth_login(request,user)
                # print("user",user)
                # print(request.user)
                # print(request.user.is_authenticated)
                return redirect('/')
    return render(request,"account/login.html")
def signup(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        password1 = request.POST.get('password1','')
        password2 = request.POST.get('password2','')
        print(request.POST)
        if name and email and password1 and password2:
            user = User.objects.create_user(name,email,password1)
            print("create user:",user)
            return redirect('/login/')
        else:
            print('please fill out all section')
    else:
        print("nothing")
    return render(request,"account/signup.html")