from django.db import models

# Create your models here.
class Logo(models.Model):
    logo = models.ImageField()

class Customer(models.Model):
    name= models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    ground = models.CharField(max_length=50)
    shift = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)
 
class Feedback(models.Model):
    fb_name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    

class Ground(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Shift(models.Model):
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.time
    
    

# class Hello(models.Model):
#     name = models.CharField(max_length=100)
#     contact = models.CharField(max_length=100)
#     def __str__(self):
#         return str(self.name)