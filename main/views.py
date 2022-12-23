from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Childern
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'Admin-home.html')

def studentlist(request):
    return render(request, 'studentlist.html')

def courselist(request):
    return render(request, 'courselist.html')

def modifycourse(request):
    return render(request, 'modifyCourse.html')

def modifystudent(request):
    return render(request, 'modifyStudent.html')

def addstudent(request):

    return render(request, 'addstu.html')

def newstu(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        name4 = name[0:4]
        yob = dob[0:4]
        pas = name4+str(yob)
        email = request.POST.get('email')
        mob = request.POST.get('mob')
        ad = request.POST.get('addr')
        data = Childern(name=name, dob=dob, email=email, pas = pas, mobile = mob, add = ad)
        data.save()
    return render(request, 'Admin-home.html')