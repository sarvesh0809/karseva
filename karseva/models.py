from django.db import models
from django.contrib.auth.models import User
# Create your models here.
User_type=(
    ('USER','USER'),
    ('SUPPLIER','SUPPLIER'),
    ('ADMIN', 'ADMIN'),
)

class UserType(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=15,choices=User_type,blank=True)
    def __str__(self):
        return f'{self.user}-{self.user_type}' 


class UserContactInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    PrimaryPhoneNumber = models.CharField(max_length=13,blank=True)
    AlternatePhoneNumber = models.CharField(max_length=13,blank=True)
    EmergencyContactNumber = models.CharField(max_length=13,blank=True)
    def __str__(self):
        return f'{self.user}' 
    
