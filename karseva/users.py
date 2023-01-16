from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from. searializer import ServiceRequest_searializer
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers
@login_required(login_url='login')
def userprofile(request):
    context={

    }

    return render(request, 'user/userprofile.html', context)

@login_required(login_url='login')
def submit_new_request(request):
    context={

    }
    return render(request, 'user/submit_new_request.html', context)

@login_required(login_url='login')
def view_user_request(request,pk):
    data=ServiceRequest.objects.get(id=pk)
    request_data = ServiceRequest_searializer(data,many=False)
    context={
        'request_data':request_data,
    }
    return render(request, 'user/view_request.html', context)

@login_required(login_url='login')
def user_request_submit(request):
    response_data={}
    try:
        category = request.POST.get('category')
        description = request.POST.get('description')
        time_in = request.POST.get('time_in')
        time_out = request.POST.get('time_out')
        volunteer = request.POST.get('volunteer')
        print(volunteer)
        if time_in and time_out and volunteer!='undefined':
            ServiceRequest.objects.create(requestor=request.user,subCategory=ServiceSubCategory.objects.get(subCategoryName=category),description=description,requestTimeInBound=time_in,requestTimeOutBound=time_out,volunteer=User.objects.get(id=volunteer))
        elif volunteer!='undefined' and not (time_in and time_out):
            ServiceRequest.objects.create(requestor=request.user,subCategory=ServiceSubCategory.objects.get(subCategoryName=category),description=description,volunteer=User.objects.get(id=volunteer))
        else:
            ServiceRequest.objects.create(requestor=request.user,subCategory=ServiceSubCategory.objects.get(subCategoryName=category),description=description)
        response_data['message'] = 200
    except Exception as e:
        print(e)
        response_data['message'] = 400

    return HttpResponse(json.dumps(response_data), content_type="application/json")

@login_required(login_url='login')
def load_request_data(request,pk):
    offset=pk
    data=ServiceRequest.objects.select_related().filter(requestor=request.user).order_by("-id")[offset:offset+10]
    request_data = ServiceRequest_searializer(data,many=True)
    json_data = json.dumps((request_data.data))

    return JsonResponse(json_data,safe=False)

    
@login_required(login_url='login')
def view_user_request_submit(request):
    context={

    }
    return render(request, 'user/submit_new_request.html', context) 