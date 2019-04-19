from django.db import models

class Article(models.Model):
    """Article model."""
    heading = models.CharField(max_length=100)
    body = models.TextField(blank=False)
