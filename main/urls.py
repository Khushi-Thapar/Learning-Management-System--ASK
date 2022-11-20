from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="mainIndex"),
    path('studentlist/', views.studentlist, name="studentlist"),
    path('courselist/', views.courselist, name="courselist"),
    path('modifycourse/', views.modifycourse, name="modifycourse"),
]
