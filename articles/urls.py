from django.urls import path
from . import views

# articles/__
urlpatterns = [
    path('create/', views.create),
    path('index/', views.index),
    path('new/', views.new),
]