from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.TextField(max_length=50,null=True)
    password=models.TextField(max_length=50,null=True)
    specialization=models.TextField(max_length=50,null=True)
    def __str__(self):
        return self.name

    