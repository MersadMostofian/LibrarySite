from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import userRegisterForm,userLoginForm
from django.contrib import messages
from home.models import Book
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'],password=cd['password'],email=cd['email'])
            user.first_name = cd['firstname']
            user.last_name = cd['lastname']
            user.save()
            messages.success(request,'User Registered','success')
            return redirect('home')
    else:
        form = userRegisterForm()
    return render(request,'register.htm',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = userLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'User Loged in','success')
                return redirect('home')
            else:
                messages.danger(request,'Username or Password is WRONG','danger')
    else:
        form = userLoginForm()
    return render(request,'login.htm',{'form':form})

def user_logout(request):
    logout(request)
    messages.error(request,'User Loged out','danger')
    return redirect('home')

def user_info(request):
    book = Book.objects.filter(given_to=request.user.username)
    return render(request,'info.htm',{'books':book})