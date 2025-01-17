from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'core/home.html')

def signup(request):
    if request.method=='GET':
        return render(request,'signup.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request,'signup.html',{
                    'form':UserCreationForm,
                    "error":'Username already exists'
                })
        return render(request,'signup.html',{
                    'form':UserCreationForm,
                    "error":'Password do not match'
                })
      
def tasks(request):
    return render(request,'components/base.html')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{
            'form':AuthenticationForm
        })
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'signin.html',{
                'form':AuthenticationForm,
                "error":'Username or password is incorrect'
            })
        else:
            login(request,user)
            return redirect('home')

    