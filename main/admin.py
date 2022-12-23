from django.contrib import admin

from .models import Student
from .models import Course
from .models import Childern
admin.site.register(Student)
admin.site.register(Childern)
admin.site.register(Course)
