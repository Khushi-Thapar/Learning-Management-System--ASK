from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="StudentsHome"),
    path('studentcourse/<int:id>/', views.studentcourse, name="studentcourse"),
    path('changepassword/<int:id>/', views.changepassword, name="changepassword"),
    path('updatepassword/<int:id>/', views.updatepassword, name = "updatepassword"),
    path('back/<int:id>/', views.back, name = "back"),
    path('logout/', views.logout, name="logout"),
]
