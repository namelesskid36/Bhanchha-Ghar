from django.db import models
from django.contrib.auth.models import User

class Chef(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.CharField(max_length=255, null=False)
    contact_number = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=254, null=False)
    gender = models.CharField(max_length=10, null=False)
    profile = models.ImageField(upload_to='uploads/', blank=True, null=True)
    resume = models.ImageField(upload_to='uploads/', blank=True, null=True)
    accountType = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.user