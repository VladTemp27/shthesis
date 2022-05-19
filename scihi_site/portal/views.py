from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from .forms import uploadDocument
from dashboard.models import *


# Create your views here.
@login_required(login_url="/accountapp/login")
def dashboard (request):
    user = request.user
    if request.user.is_authenticated:
        
        return render(request, "dashboard.html", {'sbar':'dashboard'})
    else:
         HttpResponse('Not Authenticated')

@login_required(login_url="/accountapp/login")
def documents(request):
    user = request.user
    if request.method == 'POST':
        form = uploadDocument(request.POST, request.FILES)
        if form.is_valid():
            upload_form = form.save(commit=False)
            upload_form.uploaderID = request.user
            print(upload_form.uploaderID)
            upload_form.save()
            print('upload')
            return redirect('dashboard')
        else:
            return HttpResponse("Failed")
    else:
        form = uploadDocument
    return render(request, "documents.html", {'sbar':'documents','form':form})

@login_required(login_url="/accountapp/login")
def profile(request):
    
    studentdata = Student.objects.filter(userid = request.user).values('LRN','first_name','last_name','glevel_id')
    print(studentdata)
    for data in studentdata:
        gradelevel = data["glevel_id"]
        cleanedlevel = Subjects.objects.filter(id = gradelevel).values('level')
        print(cleanedlevel)

    # for data in studentdata:
    #     print(data.LRN)

    
    return render(request, "profile.html", {'sdata':studentdata,'glevel':cleanedlevel})


def events(request):
    return render(request, 'events.html', {'sbar': 'events'})

def subjects(request):
    studentdata = Student.objects.filter(userid = request.user).values('LRN','first_name','last_name','glevel_id')
    print(studentdata)
    for data in studentdata:
        gradelevel = data["glevel_id"]
    subjects = Subjects.objects.filter(id = gradelevel).values('subject1','subject2','subject3','subject4',)

    return render(request, 'subject.html', {'sbar': 'subjects','subjects':subjects})




