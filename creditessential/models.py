from django.db import models

# Create your models here.
class CoursesFinished(models.Model):
    semester = models.CharField(max_length=20)
    courseCode = models.CharField(max_length=20)
    courseSerial = models.CharField(max_length=20)
    courseName = models.CharField(max_length=150)
    courseType = models.CharField(max_length=100)
    credit = models.IntegerField() # to add parameter
    grade = models.CharField(max_length=20)
    finalGrade = models.CharField(max_length=20)
    class Meta:
        pass