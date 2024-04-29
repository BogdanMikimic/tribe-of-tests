from django.db import models


# Create your models here.
class Note(models.Model):
    """
    Creates user notes for the user
    """
    text = models.CharField(max_length=300)
