from django.shortcuts import render,redirect
from .forms import addBookForm,editBookForm
from django.contrib.auth.models import User
from .models import Book
from django.contrib import messages

# Create your views here.
def home(request):
    book = Book.objects.all()
    return render(request,'home.htm',{'books':book})

def addBook(request):
    if request.method == 'POST':
        form = addBookForm(request.POST,request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            Book.objects.create(name=cd['name'],author=cd['author'],publishers=cd['publishers'],publishDate=cd['publishDate'],
                               category=cd['category'],image=cd['image'],status='Y',given_to='any')
            messages.success(request,'New Book Added to library','success')
            return redirect('home')
    else:
        form = addBookForm()
    return render(request,'add.htm',{'form':form})

def detile(request,Book_id):
    book = Book.objects.get(id=Book_id)
    return render(request,'detile.htm',{'book':book})

def edit(request,Book_id):
    book = Book.objects.get(id=Book_id)
    if request.method=='POST':
        form = editBookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfuly','success')
            return redirect('home')
    else:
        form = editBookForm(instance=book)
    return render(request,'edite.htm',{'form':form})

def delete(request,Book_id):
    Book.objects.get(id=Book_id).delete()
    messages.success(request,'Successfuly','success')
    return redirect('home')

def get_book(request,Book_id):
    book = Book.objects.get(id=Book_id)
    if book.given_to == 'any':
        book.given_to = request.user.username
        book.save()
        messages.success(request,'Go To library and get This book','success')
    elif book.given_to == request.user.username:
        messages.success(request,'You already have this book','info')
    else:
        messages.error(request,'This book not in library Now','info')
    return redirect('home')

def users_get(request):
    user = User.objects.filter(is_staff=False)
    return render(request,'recruitment.htm',{'users':user})
def users_leave(request):
    user = User.objects.filter(is_staff=True,is_superuser=False)
    return render(request,'layingoff.htm',{'users':user})
def get_employee(request,user_name):
    user = User.objects.get(username=user_name)
    user.is_staff = True
    user.save()
    messages.success(request,user.username+' was hired','success')
    return redirect('users_get')

def out_employee(request,user_name):    
    user = User.objects.get(username=user_name)
    user.is_staff = False
    user.save()
    messages.success(request,user.username+' was fired','danger')
    return redirect('users_leave')
