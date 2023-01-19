from django import template
from django.contrib.auth.models import User
from ..models import VolunteerInterest,ServiceSubCategory
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