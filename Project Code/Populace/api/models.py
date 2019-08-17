from django.db import models

# Create your models here.
class Associated_course(models.Model):
    platform = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name
