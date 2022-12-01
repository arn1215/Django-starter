from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm


# Create your views here.

def home(req):
    
    q = req.GET.get('q') if req.GET.get('q') != None else ""
    rooms = Room.objects.filter(topic__name__icontains = q)

    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics}
    return render(req, 'base/home.html', context)

def room(req, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(req, 'base/room.html', context)

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

def updateRoom(req, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if req.method == 'POST':
      form = RoomForm(req.POST, instance=room)
      if form.is_valid():
        form.save()
        return redirect('home')
    
    context = {'form': form}
    return render(req, 'base/room_form.html', context)

def deleteRoom(req, pk):
  room = Room.objects.get(id=pk)
  if req.method == "POST":
    room.delete()
    return redirect('home')
  return render(req, 'base/delete.html', {'obj': room})