from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    phone_number = models.CharField(max_length= 11)
    address = models.TextField(blank= True)

    def __str__(self):
        return self.user.username
    

