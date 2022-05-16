from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.hashers import make_password, check_password

from .forms import RegisterForm
from .models import Student




# Create your views here.

def registerPage(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            sign_up = form.save(commit=False)
            sign_up.password = make_password(form.cleaned_data['password'])
            print (check_password(form.cleaned_data['password'], sign_up.password))
            sign_up.save()


    form = RegisterForm()
    context = {'form': form}
    return render(request, 's_portal/register.html', context)

def loginPage(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate  

    context = {}
    return render(request, 's_portal/login.html', context)