from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    gtin_code = models.TextField(max_length=50, unique=True)
    gtin_name = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.gtin_name
