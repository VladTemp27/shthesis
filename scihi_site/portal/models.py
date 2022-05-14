from django.db import models

# Create your models here.
class UserData(models.Model): 
 """ 
 This class saves the user id along with the Address 
 """ 
 
 userid = models.CharField(max_length=10, primary_key=True) 
 username = models.CharField(max_length=50) 