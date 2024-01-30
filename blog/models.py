from django.db import models
from django.utils import timezone



class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default='')
    date = models.DateField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.title
