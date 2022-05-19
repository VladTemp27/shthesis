from django.db import models
from account.models import Account

# Create your models here.
class Document(models.Model):
    
    uploadDate              =models.DateTimeField(verbose_name="uploadDate", auto_now_add=True)
    document                =models.FileField()
    uploaderID              =models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)

class Subjects(models.Model):
    levelchoices = (
        ('G7', 'Grade 7'),
        ('G8', 'Grade 8'),
        ('G9', 'Grade 9'),
        ('G10', 'Grade 10'),
        ('G11', 'Grade 11'),
        ('G12', 'Grade 12'),
    )

    level                   =models.CharField(max_length=200, unique=True ,null=True, choices=levelchoices)
    subject1                =models.CharField(max_length=200, null=True)
    subject2                =models.CharField(max_length=200, null=True)
    subject3                =models.CharField(max_length=200, null=True)
    subject4                =models.CharField(max_length=200, null=True)
    subject5                =models.CharField(max_length=200, null=True)
    subject6                =models.CharField(max_length=200, null=True)
    subject7                =models.CharField(max_length=200, null=True)
    subject8                =models.CharField(max_length=200, null=True)
    subject9                =models.CharField(max_length=200, null=True)
    subject10               =models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.level

class Student(models.Model):
    LRN                 =models.CharField(max_length=100, unique=True,null=False)
    userid              =models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    first_name          =models.CharField(max_length=20, null=True)
    middle_name         =models.CharField(max_length=20, null=True)
    last_name           =models.CharField(max_length=20, null=True)
    glevel              =models.ForeignKey(Subjects, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name


    

    