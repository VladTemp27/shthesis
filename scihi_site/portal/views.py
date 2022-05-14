from django.shortcuts import render 
from .models import UserData 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout 
 
def show_map(request): 
 """ 
 :return: 
 """ 
 user = authenticate(userid=request.POST.get('username')) 
 if user is not None and user.is_active: 
  login(request, user) 
  return render(request, 'loadmap/loadmap.html') 
 else: 
  return HttpResponse('Error') 