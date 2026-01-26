from django.conf import settings
from django.db import models
from django.utils import timezone
# This includes the data models of your application; all Django applications need to 
# have a models.py file but it can be left empty.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return (super().get_queryset().filter(status = Post.Status.PUBLISHED))

class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'PUBLISHED'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,choices=Status,default=Status.DRAFT)
    #foreign key for author
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        # it's look like author.blog_post
        related_name='blog_post'
    )

    objects  = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['publish'] # ordering attribute to tell Django that it should sort results by the publish field
        indexes = [models.Index(fields=['-publish']),]

    def __str__(self):
        return self.title


