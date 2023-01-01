from django.shortcuts import render
from django.http import HttpResponse
from main.models import Childern
from main.models import Notices
from main.models import Course
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
    data = cvar.course
    text = str(data)
    text1 = text.split()
    a = Course.objects.get(course_id=text1[1])
    print(a.link)
    if (cvar.status == False):
        cvar.status = True
    context = {}
    context.update({'cvar': cvar})
    context.update({'a': a})
    return render(request, 'studentdashboard.html', context)


def viewnotices(request, id):
    notices = Notices.objects.filter(course_id = id)
    c = Course.objects.get(id = id)
    cid = c.course_id
    cvar = Childern.objects.get(course=id)
    context = {}
    context.update({'cvar': cvar})
    context.update({'notices':notices})
    context.update({'cid': cid})
    return render(request, 'viewnotices.html', context)

