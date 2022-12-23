from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Childern
from .models import Course
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

def addcourse(request):
    return render(request, 'addcourse.html')

def newcourse(request):
    if request.method == "POST":
        cname = request.POST.get('cname')
        cid = request.POST.get('cid')
        data = Course(course_name = cname, course_id=cid)
        data.save()
    return render(request, 'addcourse.html')


def changecourse(request):
    if request.method == "POST":
        cname = request.POST.get('Cname')
        cid = request.POST.get('Ccode')
        nname = request.POST.get('Nname')
        nid = request.POST.get('Ncode')
        if (Course.objects.filter(course_name=cname, course_id=cid).exists()):
            t = Course.objects.get(course_id = cid)
            t.course_name = nname
            t.course_id = nid
            t.save()
            return render(request, 'modifyCourse.html')
        return render(request, 'Admin-home.html')
    return render(request, 'Admin-home.html')

def changestd(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        if (Childern.objects.filter(id = id).exists()):
            phone = Childern.objects.get(mobile=request.session["user_id"])
