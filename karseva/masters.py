from django.contrib.auth.models import User
from .models import UserContactInfo,UserType,RequestStatus
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
import json
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def saveRatings(request):
    response_data ={}
    statusName = request.POST.get('statusName','')
    try:
        if not RequestStatus.objects.filter(statusName=statusName).exists() and statusName!='':
            RequestStatus.objects.create(statusName=statusName)
            response_data['message'] = f'Status has been added successfully'
        else:
            response_data['message'] = f'Status name already exsists'
    except Exception as e:
        print(e)
    return HttpResponse(json.dumps(response_data), content_type="application/json")