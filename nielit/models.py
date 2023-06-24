from django.db import models

# Create your models here.
class c_intro(models.Model):
    c_name = models.CharField(max_length=50)
    c_detail = models.CharField(max_length=1000)

    def __str__(self):
        return self.c_name