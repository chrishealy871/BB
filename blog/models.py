from __future__ import unicode_literals
from django.utils import timezone
from django.db import models



# Create your models here.
class Post(models.Model):

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=30)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    category = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title