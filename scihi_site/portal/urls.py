from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard" ),
    path('documents', views.documents, name="documents"),
    path('subjects', views.subjects, name='subjects'),
    path('events', views.events, name='events'),
    path('profile', views.profile, name='profile'),
]