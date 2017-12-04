# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User


class BlogTests(TestCase):
    def setUp(self):
        self.user = User(username='alpha', email='alpha@dragon.com')
        self.user.set_password('lizards')
        self.user.save()

    def test_post_saved_without_publish_date_set(self):
        blog = Blog(title="Words are Wind", body='', author=self.user, status='draft')
        blog.save()
        self.assertIsNone()
        blog.status = 'published'
        blog.save()