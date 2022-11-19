from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req, 'home.html')

def shop(req):
    return render(req, 'shop.html')