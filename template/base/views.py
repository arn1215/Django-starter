from django.shortcuts import render
from django.http import HttpResponse


rooms = [
  {'id': 1, 'name': 'mahogany room'},
  {'id': 2, 'name': 'tobacco room'},
  {'id': 3, 'name': 'clovewood room'},
]
# Create your views here.



def home(req):
    context = {'rooms': rooms}
    return render(req, 'base/home.html', context)

def room(req):
    item = {'name': 'sample'}
    return render(req, 'room.html', {'item': item})