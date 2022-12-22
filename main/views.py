from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'Admin-home.html')

def studentlist(request):
    return render(request, 'studentlist.html')

def courselist(request):
    return render(request, 'courselist.html')

def modifycourse(request):
    return render(request, 'modifyCourse.html')\

def modifystudent(request):
    return render(request, 'modifyStudent.html')