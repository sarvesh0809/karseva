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
            ServiceRequest.objects.create(requestor=request.user,subCategory=ServiceSubCategory.objects.get(subCategoryName=category),description=description,requestTimeInBound=time_in,requestTimeOutBound=time_out,volunteer=User.objects.get(id=volunteer),requestStatus=RequestStatus.objects.get(id=1))
        elif volunteer!='undefined' and not (time_in and time_out):
            ServiceRequest.objects.create(requestor=request.user,subCategory=ServiceSubCategory.objects.get(subCategoryName=category),description=description,volunteer=User.objects.get(id=volunteer),requestStatus=RequestStatus.objects.get(id=1))
        else:
            ServiceRequest.objects.create(requestor=request.user,subCategory=ServiceSubCategory.objects.get(subCategoryName=category),description=description,requestStatus=RequestStatus.objects.get(id=1))
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
def user_view_request_submit(request,pk):
    response_data={}
    try:
        sr = ServiceRequest.objects.get(id=pk)
        sr.description = request.POST.get('description')
        if request.POST.get('time_in'):
            sr.requestTimeInBound = request.POST.get('time_in')
        if request.POST.get('time_out'):
            sr.requestTimeOutBound = request.POST.get('time_out')
        if request.POST.get('status')=='CLOSED':
            sr.requestStatus = RequestStatus.objects.get(id=6)
       
        if request.POST.get('user_feedback')!='' and request.POST.get('status')=='CLOSED':
            sr.userFeedback=request.POST.get('user_feedback')
        if request.POST.get('user_rating')!='' and request.POST.get('status')=='CLOSED':
            
            if sr.userRating==None or sr.userRating=='':
                sr.userRating=Rating.objects.get(ratingNumber=request.POST.get('user_rating')) 
                if UserRatings.objects.filter(user = User.objects.get(username=sr.volunteer.username)).exists():
                    user = UserRatings.objects.get(user=User.objects.get(username=sr.volunteer.username))
                else:
                    user = UserRatings.objects.create(user=User.objects.get(username=sr.volunteer.username))
                user = UserRatings.objects.get(user=User.objects.get(username=sr.volunteer.username))
                user.ratingNumber+=int(request.POST.get('user_rating'))
                user.ratingCount+=1
                user.save()
        sr.save()
        response_data['message'] = 200

        
    except Exception as e:
        print(e)
        response_data['message'] = 400

    return HttpResponse(json.dumps(response_data), content_type="application/json")
