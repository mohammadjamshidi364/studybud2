from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from django.http import HttpResponse

from .forms import RegisterForm , UpdateUser
from .models import *



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
    rooms = Room.objects.all()
    
    context = {'rooms':rooms}
    return render(request , 'base/home.html', context )


def room(request , pk):
    
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request , 'base/room.html' , context)


def createRoom(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        topic_name, create = Topics.objects.get_or_create(name=topic)
        name = request.POST.get('name')
        description = request.POST.get('description')
    
    
        room = Room.objects.create(
            host = request.user,
            topic = topic_name,
            name = name , 
            description = description,
        )
        
        return redirect('home')
    context = {}
    return render(request , 'base/create_room.html' , context)


def updateRoom(request , pk):
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!!')
    if request.method == "POST":
        
        topic = request.POST.get("topic")
        topic_name , create = Topics.objects.get_or_create(name=topic)
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        room.topic = topic_name
        room.name = name
        room.description = description
        room.save()
        
        return redirect('home')
    
    context = {"room":room}
    return render(request , 'base/update_room.html', context)


def deleteRoom(request , pk):
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    context = {'room':room}
    return render(request , 'base/delete_room.html', context)