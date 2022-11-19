from django.shortcuts import render
from django.http import HttpResponse


items = [
  {'id': 1, 'name': 'mahogany'},
  {'id': 2, 'name': 'tobacco'},
  {'id': 3, 'name': 'clovewood'},
]
# Create your views here.
def home(req):
    return render(req, 'home.html')

def shop(req, pk):
    item = None
    for i in items:
      if i["id"] == int(pk):
        item = i
    return render(req, 'shop.html', {'item': item})