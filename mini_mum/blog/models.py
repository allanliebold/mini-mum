# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    """Category model."""

    name = model.CharField(max_length=25)


class Blog(models.Model):
    """Blog model."""

    title = models.CharField(max=150)
    body = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='posts')
    category = models.ManyToManyField(Category)
    STATUSES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('private', 'Private'),
    ]
    status = models.CharField(choices=STATUSES, max_length=10)

    def __repr__(self):
        """."""
        return f"<Blog Post { self.title }>"

    def __str__(self):
        """"."""
        return self.title


@receiver(post_save, sender=Blog)
def date_pub_save(instance, **kwargs):
    """."""
    if not instance.date_published and instance.status == 'published':
        instance.date_published = datetime.now()
        instance.save()
