from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
import json
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

def user_request_submit(request):
    response_data={}
    try:
        category = request.POST.get('category')
        description = request.POST.get('description')
        time_in = request.POST.get('time_in')
        time_out = request.POST.get('time_out')
        volunteer = request.POST.get('volunteer')
        if time_in and time_out and volunteer!='':
            ServiceRequest.objects.create(requestor=request.user,subCategory=ServiceSubCategory.objects.get(subCategoryName=category),description=description,requestTimeInBound=time_in,requestTimeOutBound=time_out,volunteer=User.objects.get(id=volunteer))
        elif volunteer!='' and not (time_in and time_out):
            ServiceRequest.objects.create(requestor=request.user,subCategory=ServiceSubCategory.objects.get(subCategoryName=category),description=description,volunteer=User.objects.get(id=volunteer))
        else:
            ServiceRequest.objects.create(requestor=request.user,subCategory=ServiceSubCategory.objects.get(subCategoryName=category),description=description)
        response_data['message'] = 200
    except Exception as e:
        print(e)
        response_data['message'] = 400

    return HttpResponse(json.dumps(response_data), content_type="application/json")
    