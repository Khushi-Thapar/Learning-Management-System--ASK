from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="mainIndex"),
    path('studentlist/', views.studentlist, name="studentlist"),
    path('courselist/', views.courselist, name="courselist"),
    path('modifystudent/', views.modifystudent, name="modifystudent"),
    path('addstudent/', views.addstudent, name="addstudent"),
    path('newstu/', views.newstu, name="newstu"),
    path('dropstu/', views.dropstu, name="dropstu"),
    path('dropcourse/', views.dropcourse, name="dropcourse"),
    path('newcourse/', views.newcourse, name="newcourse"),
    path('changestd/', views.changestd, name="changestd"),
    path('changecourse/', views.changecourse, name="changecourse"),
    path('addcourse/', views.addcourse, name="addcourse"),
    path('modifycourse/', views.modifycourse, name="modifycourse"),
    path('delete/<int:id>', views.delete, name='delete'),
]
