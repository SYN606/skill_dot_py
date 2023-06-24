from django.db import models

# Create your models here.


class O_level(models.Model):
    ques = models.CharField(max_length=50)
    ans = models.CharField(max_length=1000)

    def __str__(self):
        return self.name