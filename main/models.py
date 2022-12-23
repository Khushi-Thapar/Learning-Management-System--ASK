from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_id = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.course_name+" "+self.course_id

class Student(models.Model):
    name=models.CharField(max_length=200)
    course_id= models.ForeignKey(Course, null=True, default=0, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name+" "+self.course_id

class Childern(models.Model):
    name = models.CharField(max_length=50, null=True)
    dob= models.DateField()
    email = models.CharField(max_length=50)
    pas = models.CharField(max_length=200)
    mobile= models.IntegerField()
    add= models.TextField()