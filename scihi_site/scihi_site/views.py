from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#for rendering templates without passing data
def index(request):
    return render(request, 'index.html')

#for rendering templates for passing data
def index2(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def about(request):
    return render(request, "about.html")

@login_required(login_url="/accountapp/login")
def portal(request):
    user = request.user
    if request.user.is_authenticated:
        return render(request, "portal.html")
    else:
        HttpResponse('Not Authenticated')

def c19respo(request):
    return render(request, "c19.html")

def jhs(request):
    return render(request, "jhs.html")

def clubs(request):
    return render(request, "clubs.html")

def shs (request):
    return render(request, "shs.html")


def alumnitracing(request):
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSdMrCgkbzxvZuQ3xYWdR9_bqoVotBEBP3kvNgQzQjA_o6vt0g/viewform?usp=sf_link'
    return HttpResponseRedirect(url)

def toc(request):
    return render(request, "TOC.html")