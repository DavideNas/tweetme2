from django.db import models

# Create your models here.
class Tweet(models.Model):
    # id = models.AutoFiels(primary_key=True)
    content = models.TextField()