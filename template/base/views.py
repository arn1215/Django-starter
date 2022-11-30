from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


rooms = [
  {'id': 1, 'name': 'mahogany room'},
  {'id': 2, 'name': 'tobacco room'},
  {'id': 3, 'name': 'clovewood room'},
]


# Create your views here.

def home(req):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(req, 'base/home.html', context)

def room(req, pk):
    room = None
    for i in rooms:
      if i['id'] == int(pk):
        room = i
    context = {'room': room}
    return render(req, 'base/room.html', context)