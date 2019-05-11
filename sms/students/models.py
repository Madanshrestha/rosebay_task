from django.db import models

from schools.models import School

# Create your models here.

class Student(models.Model):
    school = models.ForeignKey('schools.School', related_name='students', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.student_name