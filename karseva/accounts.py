from django.contrib.auth.models import User
from .models import UserContactInfo,UserType
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

import json

def userLogin(request):
    response_data ={}
    username = request.POST.get('username')
    password = request.POST.get('password')
    if User.objects.filter(username=username).exists():
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                response_data['message'] = 200

            else:
                response_data['message'] = 'Login failed, Please check your credentials' 
    else:
        response_data['message'] = f'No account exsists for {username}'
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def userSignup(request):
    if request.method=='POST':
        response_data ={}
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            firstName = request.POST.get('firstName','')
            lastName = request.POST.get('lastName','')
            userType = request.POST.get('userType','USER')
            phoneNumber = request.POST.get('phoneNumber','')
            # alternatePhoneNumber = request.POST.get('alternatePhoneNumber','')
            # emergencyContactNumber = request.POST.get('emergencyContactNumber','')
            user = User.objects.create(username= email,password=make_password(password),first_name=firstName,last_name=lastName)
            UserType.objects.create(user=user,user_type=userType,)
            UserContactInfo.objects.create(user=user,primaryPhoneNumber=phoneNumber)
            response_data['message'] = 200
        except Exception as e:
            response_data['message'] = f'{e}'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    

def checkEmail(request):
    response_data ={}
    email = request.POST.get('email',None)
    phoneNumber = request.POST.get('phoneNumber',None)
    response_data['message'] = 400
    if email:
        if User.objects.filter(email=email).exists():
            response_data['message'] = 400
        else:
            response_data['message'] = 200
    elif phoneNumber:
        if UserContactInfo.objects.filter(primaryPhoneNumber=phoneNumber).exists():
            response_data['message'] = 400
        else:
            response_data['message'] = 200
    return HttpResponse(json.dumps(response_data), content_type="application/json")
    





