from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

#for rendering templates without passing data
def index(request):
    return render(request, 'index.html')

#for rendering templates for passing data
def index2(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def about(request):
    return render(request, "about.html")

def portal(request):
    return render(request, "portal.html")

def c19respo(request):
    return render(request, "c19.html")