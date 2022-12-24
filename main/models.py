from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_id = models.CharField(max_length=200, primary_key=True)
    def __str__(self) -> str:
        return self.course_name+" "+self.course_id


class Childern(models.Model):
    #course = models.ForeignKey(Course, db_column='course_id', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    dob= models.DateField()
    email = models.CharField(max_length=50)
    pas = models.CharField(max_length=200)
    mobile= models.IntegerField()
    add= models.TextField()


