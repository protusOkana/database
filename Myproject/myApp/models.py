from django.db import models

# Create your models here.
class student(models.Model):
    FirstName= models.CharField (max_length=50)  
    SecondName= models.CharField (max_length=100) 
    email=models.EmailField()
    regNo= models.TextField()
    Age = models.IntegerField()

    def __str__(self):
        return self.FirstName
    