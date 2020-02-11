from django.db import models


# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=100, blank=True)
    url = models.URLField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.title