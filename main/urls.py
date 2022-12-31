from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="mainIndex"),
    path('studentlist/', views.studentlist, name="studentlist"),
    path('courselist/', views.courselist, name="courselist"),
    path('notification/', views.notification, name="notification"),
    path('pushnotice/', views.pushnotice, name = "pushnotice"),
    path('pushednotices/<int:id>/', views.pushednotices, name="pushednotices"),
    path('modifystudent/', views.modifystudent, name="modifystudent"),
    path('addstudent/', views.addstudent, name="addstudent"),
    path('newstu/', views.newstu, name="newstu"),
    path('dropstu/', views.dropstu, name="dropstu"),
    path('dropcourse/', views.dropcourse, name="dropcourse"),
    path('newcourse/', views.newcourse, name="newcourse"),
    path('changestd/', views.changestd, name="changestd"),
    path('changecourse/', views.changecourse, name="changecourse"),
    path('downloadcsv/', views.getdata, name="downloadcsv"),
    path('addcourse/', views.addcourse, name="addcourse"),
    path('modifycourse/', views.modifycourse, name="modifycourse"),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('delete1/<int:id>', views.delete1, name='delete1'),
    path('deletenotice/<int:id>', views.deletenotice, name='deletenotice'),
    path('validiate/', views.validiate, name = "validiate"),
    path('changeadminpassword/', views.changeadminpassword, name = "changeadminpassword"),
    path('updateadminpass/', views.updateadminpass, name="updateadminpass"),
    path('back/', views.back, name = "back"),
    path('upload/<int:id>/', views.upload, name = 'upload'),
    path('home/', views.home, name="home"),
    path('attend/<int:id>/', views.attendance, name='attend'),
    path('markattend/<int:id>/', views.markattend, name='markattend'),
    path('grades/<int:id>/', views.grades, name='grades'),
    path('markgrades/<int:id>/', views.markgrades, name='markgrades'),
    path('downloadcoursecsv/<int:id>/', views.downloadcoursecsv, name='downloadcoursecsv'),

]
