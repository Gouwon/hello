from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField(
        verbose_name='SLUG', unique=True, 
        allow_unicode=True, help_text='one word for title alias.'
    )
    description = models.CharField(
        verbose_name='DESCRIPTION', max_length=100,
        blank=True, help_text='simple decription text.'
    )
    content = models.TextField(verbose_name='CONTENT')
    create_dt = models.DateTimeField(
        verbose_name='CREATE DATE', auto_now_add=True
    )
    modify_dt = models.DateTimeField(
        verbose_name='MODIFY DATE', auto_now=True
    )
    tags = TaggableManager(blank=True)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt', )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:detail', args=(self.slug,))
    
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    
    def get_next(self):
        return self.get_next_by_modify_dt()