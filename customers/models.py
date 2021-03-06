from django.db import models

# Create your models here.


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
    price=models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Shift(models.Model):
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.time
    
    
class Gallery(models.Model):
    image = models.ImageField()

class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    



# class Hello(models.Model):
#     name = models.CharField(max_length=100)
#     contact = models.CharField(max_length=100)
#     def __str__(self):
#         return str(self.name)