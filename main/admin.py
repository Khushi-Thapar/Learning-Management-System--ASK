from django.contrib import admin

from .models import Notices
from .models import Course
from .models import Childern
from .models import Admin
admin.site.register(Childern)
admin.site.register(Course)
admin.site.register(Notices)
admin.site.register(Admin)
