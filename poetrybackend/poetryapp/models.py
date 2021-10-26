from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class Poem(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    poemtext = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.title} by {self.author}"