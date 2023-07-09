from django.db import models

# Create your models here.

class Partner(models.Model):
    partner_name = models.CharField(max_length=50)
    partner_details = models.TextField()
    partner_social_media_link = models.CharField(max_length=50, null=True, blank=True)
    partner_logo = models.ImageField()
    
    def __str__(self) -> str:
        return self.partner_name