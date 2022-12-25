from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_id = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.course_name+" "+self.course_id

class Childern(models.Model):
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    dob = models.DateField()
    email = models.CharField(max_length=50)
    pas = models.CharField(max_length=200)
    mobile = models.IntegerField()
    add = models.TextField()
