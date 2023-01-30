from django import template
from django.contrib.auth.models import User
from django.db.models import Sum
from ..models import VolunteerInterest,ServiceSubCategory,ServiceRequest
import datetime
register = template.Library()

@register.filter
def volunteerCheck(id):
    try:
        return User.objects.get(id=id).username
    except Exception as e:
        return 'N/A'
    

import dateutil.parser


@register.filter   
def formatDate(value):
    print(value)
    return datetime.datetime.strptime(value,"%Y-%m-%dT%H:%M:%S%z").isoformat()


@register.filter   
def checkInterest(value,arg):
    if value=='health_related':
        return VolunteerInterest.objects.filter(volunteer__id=arg).filter(interest__serviceCategory__serviceName='Health').exists()
    if value=='daily_needs':
        return VolunteerInterest.objects.filter(volunteer__id=arg).filter(interest__serviceCategory__serviceName='Daily Needs').exists()
    if value=='information_guidance':
        return VolunteerInterest.objects.filter(volunteer__id=arg).filter(interest__serviceCategory__serviceName='Information Guidance').exists()
    if value=='psychological_support':
        return VolunteerInterest.objects.filter(volunteer__id=arg).filter(interest__serviceCategory__serviceName='Psychological Support').exists()
    

    else:
        return False
    

@register.filter
def category_list(val):
    return ServiceSubCategory.objects.values_list('subCategoryName',flat=True)


@register.filter   
def trackTask(id,value):
    if value=='ALL':
        return ServiceRequest.objects.filter(volunteer__id=id).count()
    else:
        return ServiceRequest.objects.filter(volunteer__id=id).filter(requestStatus__statusName=value).count()


@register.simple_tag
def add(a, b):
    return a + b

@register.filter   
def volunteer_point(id):
    try:
        return ServiceRequest.objects.filter(volunteer__id=id).aggregate(Sum('volunteerPoint'))['volunteerPoint__sum']
    except Exception as e:
        print(e)
        return 0