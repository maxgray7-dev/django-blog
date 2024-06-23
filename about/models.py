from django.db import models

# Create your models here.

class About(models.Model):
    # 
    title = models.CharField(max_length=200, unique=True)
    context = models.TextField(max_length=200, unique = True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title