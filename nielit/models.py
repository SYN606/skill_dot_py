from django.db import models

# Create your models here.
class c_intro(models.Model):
    c_name = models.CharField(max_length=50)
    c_detail = models.TextField(max_length=1000)

    def __str__(self):
        return self.c_name
    

class Module(models.Model):
    course_name = models.ForeignKey(c_intro, on_delete=models.CASCADE)

    module_code = models.CharField(max_length=50, blank=True, null=True)
    module_name = models.CharField(max_length=50)
    module_detail =  models.TextField()

    def __str__(self):
        return self.module_name
