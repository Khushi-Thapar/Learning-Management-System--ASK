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
    path('addcourse/', views.addcourse, name="addcourse"),
    path('modifycourse/', views.modifycourse, name="modifycourse"),
]
