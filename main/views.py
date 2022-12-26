import os

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Childern
from .models import Course
from django.http import HttpResponse
import csv
# Create your views here.



def index(request):
    return render(request, 'Admin-home.html')

def studentlist(request):
    stu_list= Childern.objects.all()
    return render(request, 'studentlist.html', {'stu_list':stu_list})

def courselist(request):
    course_list= Course.objects.all()
    return render(request, 'courselist.html',{'course_list':course_list} )

def modifycourse(request):
    return render(request, 'modifyCourse.html')

def modifystudent(request):
    course_list = Course.objects.all()
    return render(request, 'modifyStudent.html', {'course_list': course_list})

def addstudent(request):
    course_list = Course.objects.all()
    return render(request, 'addstu.html' , {'course_list': course_list})

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
        course = request.POST.get('course')
        c = Course.objects.get(course_id = course)
        data = Childern(course = c, name=name, dob=dob, email=email, pas = pas, mobile = mob, add = ad)
        data.save()
    return render(request, 'Admin-home.html')

def changestd(request):
    if request.method == "POST":
        csid = request.POST.get('sid')
        cnum = request.POST.get('newnum')
        cadd = request.POST.get('newadd')
        ccourse = request.POST.get('newcourse')
        c = Course.objects.get(course_id = ccourse)
        if (Childern.objects.filter(id=csid).exists()):
            t = Childern.objects.get(id=csid)
            t.mobile = cnum
            t.add = cadd
            t.course = c
            t.save()
            messages.success(request, 'Student Mofified Successfully!')
            return render(request, 'Admin-home.html')
        return render(request, 'Admin-home.html')
    return render(request, 'Admin-home.html')

def addcourse(request):
    return render(request, 'addcourse.html')

def newcourse(request):
    if request.method == "POST":
        cname = request.POST.get('cname')
        cid = request.POST.get('cid')
        data = Course(course_name = cname, course_id=cid)
        data.save()
        directory = cid
        parent_dir = "media/"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
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
            messages.success(request, 'Course Mofified Successfully!')
            return render(request, 'Admin-home.html')
        return render(request, 'Admin-home.html')
    return render(request, 'Admin-home.html')

def validiate(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        if (Childern.objects.filter(id = id).exists()):
            child = Childern.objects.get(id = id)
            mob = child.mobile
            print(mob)
            if (request.POST.get('option1')):
                newmob = mob
            else:
                newmob = request.POST.get('newnum')
                child.mobile = newmob
            add = child.add
            if (request.POST.get('option2')):
                newadd = add
            else:
                newadd = request.POST.get('newadd')
                child.add = newadd
    return render(request, 'Admin-home.html')


def dropstu(request):
    return render(request, 'dropstu.html')

def dropcourse(request):
    return render(request, 'dropcourse.html')

def delete(request, id):
  member = Childern.objects.get(id=id)
  member.delete()
  stu_list = Childern.objects.all()
  return render(request, 'studentlist.html' , {'stu_list': stu_list})

def delete1(request, id):
  member = Course.objects.get(id=id)
  member.delete()
  course_list = Course.objects.all()
  return render(request, 'courselist.html', {'course_list': course_list})




def getdata(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="Students.csv"'},
    )
    students = Childern.objects.all()
    writer = csv.writer(response)
    for student in students:
        writer.writerow([student.id,student.name,student.dob, student.email, student.mobile, student.add,student.course])
    return response

def back(request):
    return render(request, 'Admin-home.html')

def home(request):
    return render(request, 'index.html')
def upload(request, id):
    cvar = Course.objects.get(id = id)
    return render(request, 'fileupload.html', {'cvar': cvar})
# def uploadmedia(request, id):
#     cvar = Course.objects.get(id=id)
#     return render(request, 'fileupload.html', {'cvar': cvar})
#
# def formsubmission(request, id):
#     form = upload()
#     if request.method == "POST":
#         form = upload(request.POST,request.FILES)
#         if form.is_valid():
#             f = request.FILES['file']
#             cvar = Course.objects.get(id=id)
#             cname = cvar.course_id
#             with open('media/' + cname + '/' + f.name, 'wb+') as destination:
#                 for chunk in f.chunks():
#                     destination.write(chunk)
#             return HttpResponse("FILE UPLOADED SUCCESSFULLY")
#         else:
#             form = upload()
#             return render(request, 'Admin-home.html', {'form': form})

def notification(request):
    return render(request, 'notice.html')