from django.shortcuts import render
from django.http import HttpResponse
from main.models import Childern
from main.models import Course
from main.models import Admin
from main.models import Notices
# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("main index")

def Adminhome(request):
    mail = (request.POST.get('LoginEmail'))
    print(mail)
    pas = (request.POST.get('loginPassword'))
    if (Admin.objects.filter(email = mail, pas=pas).exists()):
        return render(request, 'Admin-home.html')
    if (Childern.objects.filter(email = mail, pas=pas).exists()):
        cvar = Childern.objects.get(email=mail)
        data = cvar.course
        text = str(data)
        text1 = text.split()
        a = Course.objects.get(course_id = text1[1])
        print(a.link)
        if(cvar.status == False):
            cvar.status = True
        context = {}
        context.update({'cvar':cvar})
        context.update({'a':a})
        return render(request, 'studentdashboard.html', context)
    else:
        return render(request, 'index.html')

def courses(request):
    course_list = Course.objects.all()
    return render(request, 'courses.html', {'course_list': course_list})

def home1(request):
    return render(request, 'index.html')

def stuhome(request, id):
    cvar = Childern.objects.get(id = id)

    return render(request, 'studentdashboard.html', {'cvar': cvar})
def pdot(request):
    return render(request, 'pdot.html')

def ircon(request):
    return render(request, 'ircon.html')

def kvic(request):
    return render(request, 'kvic.html')

def nulm(request):
    return render(request, 'nulm.html')

def pcra(request):
    return render(request, 'pcra.html')

def tmf(request):
    return render(request, 'tmf.html')


