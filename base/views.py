from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
    
    if request.user.is_authenticated:
        
        user = request.user
        
        
        if request.method == "POST":
            avatar = request.FILES.get('avatar')
            username = request.POST.get('username')
            bio = request.POST.get('bio')
            if avatar:
                user.avatar = avatar
                user.bio = bio
                user.save()
                return redirect('home')
            else:
                user.bio = bio
                user.save()
                return redirect("home")
                
            
    else:
        return redirect('home')
    
    
    context = {'user':user}
    return render(request , 'base/update_user.html' , context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | 
                                Q(name__icontains=q) |
                                Q(description__icontains=q) |
                                Q(host__username__icontains=q)
                                )
    topics = Topics.objects.all()[0:5]
    room_count = rooms.count()

    context = {'rooms':rooms , 'topics':topics , 'room_count':room_count}
    return render(request , 'base/home.html', context )


def room(request , pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by("-created")
    
    if request.method == "POST":
        body = request.POST.get('message')
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = body
        )
        return redirect('room', pk=room.id)
    
    context = {'room':room , 'messages':room_messages}
    return render(request , 'base/room.html' , context)

login_required(login_url="login")
def createRoom(request):
    topics = Topics.objects.all()
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
    context = {'topics':topics}
    return render(request , 'base/create_room.html', context)

login_required(login_url="login")
def updateRoom(request , pk):
    room = Room.objects.get(id=pk)
    topics = Topics.objects.all()
    
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
    
    context = {"room":room , 'topics':topics}
    return render(request , 'base/update_room.html', context)

login_required(login_url="login")
def deleteRoom(request , pk):
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    context = {'room':room}
    return render(request , 'base/delete.html', context)