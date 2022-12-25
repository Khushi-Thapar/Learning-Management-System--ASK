from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="StudentsHome"),
    path('studentcourse/<int:id>/', views.studentcourse, name="studentcourse"),
]
