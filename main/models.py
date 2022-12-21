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

class Register(models.Model):
    mobile= models.CharField(max_length=200)
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.email+" "+self.password+" "+self.mobile+" "+self.user_name

  