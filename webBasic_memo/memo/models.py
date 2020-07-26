from django.db import models

class Memo(models.Model):
    title = models.CharField
    content = models.CharField(max_length=100)