from django.shortcuts import render
from django.http import HttpResponse
from main.models import Childern
from RCED_Backend.views import Adminhome

# Create your views here.

def index(request):
    return render(request, 'index.html')

def studentcourse(request, id):
    if (Childern.objects.filter(id = id).exists()):
        cvar= Childern.objects.get(id = id)
        return render(request, 'stucourse.html', {'cvar': cvar})
    return render(request, 'stucourse.html')

def logout(request):
    # if (Childern.objects.filter(id = id).exists()):
    #     cvar= Childern.objects.get(id = id)
    #     cvar.status = False
    #     return render(request, 'index.html')
    return render(request, 'index.html')

def changepassword(request, id):
    cvar = Childern.objects.get(id = id)
    return render(request, 'changepassword.html', {'cvar':cvar})

def updatepassword(request, id):
    if (Childern.objects.filter(id=id).exists()):
        cvar = Childern.objects.get(id = id)
        oldpass = cvar.pas
        newpas = request.POST.get('newpass')
        if (request.POST.get('oldpass')==oldpass):
            cvar.pas = newpas
            cvar.save()
    return render(request, 'studentdashboard.html', {'cvar': cvar})

def back(request, id):
    cvar = Childern.objects.get(id=id)
    return render(request, 'studentdashboard.html', {'cvar': cvar})