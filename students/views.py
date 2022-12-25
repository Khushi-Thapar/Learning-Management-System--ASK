from django.shortcuts import render
from django.http import HttpResponse
from main.models import Childern
from RCED_Backend.views import Adminhome

# Create your views here.

def index(request):
    return HttpResponse("hello world")

def studentcourse(request, id):
    if (Childern.objects.filter(id = id).exists()):
        cvar= Childern.objects.get(id = id)
        return render(request, 'stucourse.html', {'cvar': cvar})
    return render(request, 'stucourse.html')
