from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=150, db_index=True, unique=True)
    password=models.CharField(max_length=50)
    data=models.DateTimeField(auto_now_add=True)
    access_time=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.name)
