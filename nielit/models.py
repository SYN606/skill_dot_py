from django.db import models

# Create your models here.
class c_intro(models.Model):
    c_name = models.CharField(max_length=50)
    c_detail = models.CharField(max_length=1000)

    def __str__(self):
        return self.c_name
    

class Module(models.Model):
    course_name = models.ForeignKey(c_intro, on_delete=models.CASCADE)

    module_code = models.CharField(max_length=50, blank=True, null=True)
    module_name = models.CharField(max_length=50)

    module_detail = models.CharField(max_length=500, blank=True, null=True)
    extra_md = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.module_code} | {self.module_name}"
    
class Syllabus(models.Model):
    module_name = models.ForeignKey(Module, on_delete=models.CASCADE)
    # md_name = models.ManyToManyField(Module)
    chapter_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.chapter_name} | {self.module_name}"