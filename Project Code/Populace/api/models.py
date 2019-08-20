from django.db import models
from django.conf import settings

# Create your models here.
class Associated_course(models.Model):
    platform = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    populace_user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name
