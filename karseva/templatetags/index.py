from django import template
from django.contrib.auth.models import User
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