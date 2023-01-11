from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import pytz
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
timezone.activate(pytz.timezone("Asia/Kolkata"))
timezone.localtime(timezone.now())
# Create your models here.
User_type=(
    ('USER','USER'),
    ('VOLUNTEER','VOLUNTEER'),
    ('ADMIN', 'ADMIN'),
)
Rating_choices=(
    ('EXCELLENT','EXCELLENT'),
    ('VERY GOOD','VERY GOOD'),
    ('GOOD', 'GOOD'),
    ('FAIR', 'FAIR'),
    ('POOR', 'GOOD'),
    ('VERY POOR', 'VERY POOR'),
)


class UserType(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=15,choices=User_type,blank=True)
    def __str__(self):
        return f'{self.user}-{self.user_type}' 


class UserContactInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    primaryPhoneNumber = models.CharField(max_length=13,blank=True)
    alternatePhoneNumber = models.CharField(max_length=13,blank=True)
    emergencyContactNumber = models.CharField(max_length=13,blank=True)
    def __str__(self):
        return f'{self.user}' 
    
class RequestStatus(models.Model):
    statusName = models.CharField(max_length=20,blank=True)
    isActive = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.statusName} - {self.isActive}' 
    
class ServiceCategory(models.Model):
    serviceName = models.CharField(max_length=30,blank=True)
    isActive = models.BooleanField(default=True)
    createdOn = models.DateTimeField(default=timezone.localtime(timezone.now()), blank=True)
    createdBy = CurrentUserField()
    modifiedOn = models.DateTimeField(default=timezone.localtime(timezone.now()), blank=True)
    modifiedBy = CurrentUserField(related_name='service_categor_modified_by')
    def update(self, *args, **kwargs):
        kwargs.update({'modifiedOn': timezone.localtime(timezone.now()),'modifiedBy': get_current_authenticated_user()})
        
        super().update(*args, **kwargs)
        return self

    def __str__(self):
        return f'{self.serviceName} - {self.isActive}' 
    
# print(get_current_authenticated_user)
class ServiceSubCategory(models.Model):
    subCategoryName = models.CharField(max_length=30,blank=True)
    serviceCategory = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    createdOn = models.DateTimeField(default=timezone.localtime(timezone.now()), blank=True)
    createdBy = CurrentUserField()
    modifiedOn = models.DateTimeField(default=timezone.localtime(timezone.now()), blank=True)
    modifiedBy = CurrentUserField(related_name='service_subcategor_modified_by')
    def update(self, *args, **kwargs):
        kwargs.update({'modifiedOn': timezone.localtime(timezone.now()),'modifiedBy': get_current_authenticated_user()})
        super().update(*args, **kwargs)
        return self
    def __str__(self):
        return f'{self.subCategoryName} - {self.serviceCategory.serviceName}' 


class Rating(models.Model):
    ratingName=models.CharField(max_length=15,choices=Rating_choices,blank=True)
    ratingNumber = models.IntegerField(blank=True)
    isActive = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.ratingName}'


class ServiceRequest(models.Model):
    requestor = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='requestor_name',null=True)
    subCategory = models.ForeignKey(ServiceSubCategory,on_delete=models.SET_NULL,null=True)
    volunteer = models.ForeignKey(User,on_delete=models.SET_NULL, related_name='volunteer_name',null=True)
    requestStatus = models.ForeignKey(RequestStatus,on_delete=models.SET_NULL,null=True)
    requestTimeInBound = models.DateTimeField(default=timezone.localtime(timezone.now()), blank=True)
    requestTimeOutBound = models.DateTimeField(default=timezone.localtime(timezone.now()), blank=True)
    actualTimeInBound = models.DateTimeField( blank=True)
    actualTimeOutBound = models.DateTimeField(blank=True)
    requestCreatedBy = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='request_createdby',null=True)
    requestCreatedOn = models.DateTimeField(default=timezone.localtime(timezone.now()), blank=True)
    lastModifiedBy= models.ForeignKey(User,on_delete=models.SET_NULL,related_name='last_modifiedby',null=True,blank=True)
    lastModifiedOn = models.DateTimeField(default=timezone.localtime(timezone.now()), blank=True)
    userRating = models.ForeignKey(Rating,on_delete=models.SET_NULL,related_name='user_rating',null=True,blank=True)
    volunteerRating = models.ForeignKey(Rating,on_delete=models.SET_NULL,related_name='volunteer_rating',null=True,blank=True)
    description = models.CharField(max_length=200,blank=True)
    userFeedback = models.CharField(max_length=200,blank=True)
    volunteerFeedback = models.CharField(max_length=200,blank=True)
    canceledBy = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='canceled_by',null=True,blank=True)
    cancelledOn= models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f'{self.requestor} - {self.subCategory} - {self.requestStatus.statusName} '





# pip install django-currentuser