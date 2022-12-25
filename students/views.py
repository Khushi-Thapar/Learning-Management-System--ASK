from django.shortcuts import render
from django.http import HttpResponse
from main.models import Childern

# Create your views here.

def index(request):
    return HttpResponse("hello world")

def studentcourse(request):
    mail = (request.POST.get('LoginEmail'))
    if (Childern.objects.filter(email = mail).exists()):
        cvar= Childern.objects.get(email=mail)
        return render(request, 'studentdashboard.html', {'cvar': cvar})
    return render(request, 'stucourse.html')
