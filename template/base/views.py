from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def loginPage(req): 
  page = 'login'
  print(page)
  if req.user.is_authenticated:
    return redirect('home')

  if req.method == 'POST':
    username = req.POST.get('username')
    password = req.POST.get('password')
    print(username, password)

    try:
      user = User.objects.get(username=username)
    except:
      messages.error(req, "User does not exist")

    user = authenticate(req, username=username, password=password)

    if user is not None:
      login(req, user)
      return redirect('home')
    else:
      messages.error(req, "username or password does not exist.")
      
  context = {'page': page}
  return render(req, 'base/login_register.html', context)

def logoutUser(req):
  logout(req)
  return redirect('home')

def registerPage(req):
  page = 'register'
  form = UserCreationForm()
  return render(req, 'base/login_register.html', {'form': form})

def home(req):
    
    q = req.GET.get('q') if req.GET.get('q') != None else ""
    
    rooms = Room.objects.filter(
      Q(topic__name__icontains = q) |
      Q(name__icontains = q) |
      Q(description__icontains = q)

    )

    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms': rooms, 'topics': topics, 'count': room_count}
    return render(req, 'base/home.html', context)

def room(req, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(req, 'base/room.html', context)

@login_required(login_url='login')
def createRoom(req):
  form = RoomForm()
  if req.method == 'POST':
    form = RoomForm(req.POST)
    if form.is_valid():
      form.save()
      return redirect('home')

    print(req.POST)
  context = {'form': form}
  return render(req, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(req, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if req.user != room.host:
      return HttpResponse("Oops you're not suppose to be here...")

    if req.method == 'POST':
      form = RoomForm(req.POST, instance=room)
      if form.is_valid():
        form.save()
        return redirect('home')
    
    context = {'form': form}
    return render(req, 'base/room_form.html', context)

def deleteRoom(req, pk):
  room = Room.objects.get(id=pk)

  if req.user != room.host:
    return HttpResponse("Oops you're not suppose to be here...")

  if req.method == "POST":
    room.delete()
    return redirect('home')
  return render(req, 'base/delete.html', {'obj': room})