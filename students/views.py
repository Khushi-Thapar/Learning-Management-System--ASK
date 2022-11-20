from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'studentdashboard.html')

def studentcourse(request):
    # return render(request, 'stucourse.html')
    return HttpResponse("hello world")