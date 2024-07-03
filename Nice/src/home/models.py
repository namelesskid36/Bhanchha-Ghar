from django.db import models
from django.contrib.auth.models import User




class Room(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    img = models.FileField(upload_to='static/uploads')  # FileField for uploading images
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.CharField(default="null" , max_length=255, null=False)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.CharField(max_length=255, null=False)
    contact_number = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=254, null=False)
    gender = models.CharField(max_length=10, null=False)
    profile = models.ImageField(upload_to='static/pfps', blank=True, null=True)
    resume = models.ImageField(upload_to='static/Resumes', blank=True, null=True)
    accountType = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.user