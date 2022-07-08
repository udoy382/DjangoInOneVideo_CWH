from django.db import models

# Create your models here.

class Contact(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=12)
    Password = models.CharField(max_length=150)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.FirstName
