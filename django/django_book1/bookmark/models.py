from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=100, blank=True)
    url = models.URLField(verbose_name='URL', unique=True)
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, blank=True, null=True
    )
    
    def __str__(self):
        return self.title