from django.shortcuts import render
from django.http import HttpResponse
from main.models import Childern
from main.models import Course
# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("main index")

def Adminhome(request):
    mail = (request.POST.get('LoginEmail'))
    print(mail)
    pas = (request.POST.get('loginPassword'))
    if mail == 'admin@gmail.com' and pas == 'admin':
        return render(request, 'Admin-home.html')
    if (Childern.objects.filter(email = mail, pas=pas).exists()):
        cvar= Childern.objects.get(email=mail)
        if(cvar.status == False):
            cvar.status = True
            return render(request, 'studentdashboard.html', {'cvar': cvar})
    else:
        return render(request, 'index.html')

def courses(request):
    course_list = Course.objects.all()
    return render(request, 'courses.html', {'course_list': course_list})

def home1(request):
    return render(request, 'index.html')