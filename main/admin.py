from django.contrib import admin


from .models import Course
from .models import Childern
admin.site.register(Childern)
admin.site.register(Course)
