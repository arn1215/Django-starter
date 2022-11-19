from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('shop/<str:pk>/', views.shop, name="shop"),
]