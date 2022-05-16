from enum import auto
from django.db import models

# Create your models here.
class UserData(models.Model):
    userid = models.CharField(max_length=10, primary_key=True) 
    username = models.CharField(max_length=50) 
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.userid

class Student(models.Model):
    username = models.CharField(max_length = 10, null=True)
    password = models.CharField(max_length= 300, null=True)

    def __str__(self):
        return self.username