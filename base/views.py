from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages

from .forms import RegisterForm , UpdateUser
from .models import User



def registerPage(request):
    form = RegisterForm()
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect('home')
    context = {'form': form}
    return render(request , 'base/register.html' , context)

def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
            
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            try:
                user = User.objects.get(username=username)
            except:
                user = User.objects.get(email=username)
        except:
            messages.error(request , "User does not exist")
            return redirect('login')
        
        authenticate_user = authenticate(request , username=user.username , password=password)

        if authenticate_user is not None:
            login(request , authenticate_user)
            return redirect('home')
    return render(request , 'base/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')

def updateUser(request):
    user = request.user
    form = UpdateUser(instance=user)
    
    
    
    context = {'form':form , 'user':user}
    return render(request , 'base/update_user.html' , context)


def home(request):
    
    
    return render(request , 'base/home.html')