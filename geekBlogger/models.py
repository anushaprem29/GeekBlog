from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class geekblogdb(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey('auth.User', default=0)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

