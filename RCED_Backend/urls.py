"""RCED_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='homepage'),
    path("home1", views.home1, name = "home1"),
    path('main/', include("main.urls")),
    path('studentlist/', include("main.urls")),
    path('courses/', views.courses, name = "courses"),
    path('pdot/', views.pdot, name = "pdot"),
    path('ircon/', views.ircon, name = "ircon"),
    path('kvic/', views.kvic, name = "kvic"),
    path('nulm/', views.nulm, name = "nulm"),
    path('pcra/', views.pcra, name = "pcra"),
    path('tmf/', views.tmf, name = "tmf"),
    path('addcourse/', include("main.urls")),
    path('courselist/', include("main.urls")),
    path('modifycourse/', include("main.urls")),
    path('studentcourse/', include("students.urls")),
    path('addstudent/', include("main.urls")),
    path("Adminhome/", views.Adminhome, name='Admin-login'),
    path('logout/', include("students.urls")),
    path('students/', include("students.urls")),
    path('home/', include("main.urls")),
    path('stuhome/<int:id>', views.stuhome, name = "stuhome"),
    path('notification/', include("main.urls")),
    path('attend', views.attendance, name='attend'),
    path('grades', views.grades, name='grades')
]
