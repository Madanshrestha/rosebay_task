from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=255)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.school_name