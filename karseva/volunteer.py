from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest,UserContactInfo,RequestStatus,Rating,User,UserRatings,VolunteerInterest,ServiceSubCategory
from .searializer import ServiceRequest_searializer
import json

# Create your views here.
@login_required(login_url='login')
def user_requests(request):
    services = ServiceRequest.objects.all()
    context={
        "services":services
    }
    return render(request, 'volunteer/requests.html', context)

@login_required(login_url='login')
def volunteer_view_page(request):
    services = ServiceRequest.objects.all()
    context={
        "services":services
    }
    return render(request, 'volunteer/volunteer_view_page.html', context)

@login_required(login_url='login')
def volunteerprofile(request):
    volprofiles = UserContactInfo.objects.all()
    context={
        "volprofile":volprofiles
    }
    return render(request, 'volunteer/volunteerprofile.html', context)



@login_required(login_url='login')
def load_volunteer_data(request,pk):
    offset=pk
    data=ServiceRequest.objects.select_related().filter(volunteer=request.user).order_by("-id")[offset:offset+10]
    request_data = ServiceRequest_searializer(data,many=True)
    json_data = json.dumps((request_data.data))
    return JsonResponse(json_data,safe=False)

@login_required(login_url='login')
def view_user_request_volunteer(request,pk):
    data=ServiceRequest.objects.get(id=pk)
    request_data = ServiceRequest_searializer(data,many=False)
    context={
        'request_data':request_data,
    }
    return render(request, 'volunteer/view_request.html', context)




@login_required(login_url='login')
def volunteer_view_request_submit(request,pk):
    response_data={}
    try:
        sr = ServiceRequest.objects.get(id=pk)
        print(request.POST.get('actual_time_in'))
        if request.POST.get('status')!='CLOSED':
            sr.requestStatus = RequestStatus.objects.get(statusName=request.POST.get('status'))
        if request.POST.get('actual_time_in')!='':
            sr.actualTimeInBound = request.POST.get('actual_time_in')
        if request.POST.get('actual_time_out')!='':
            sr.actualTimeOutBound = request.POST.get('actual_time_out')
        if request.POST.get('volunteer_feedback')!='' and request.POST.get('status')=='CLOSED' :
            sr.volunteerFeedback=request.POST.get('volunteer_feedback')
        if request.POST.get('volunteer_rating')!='' and request.POST.get('status')=='CLOSED':
            if sr.volunteerRating==None or sr.volunteerRating=='':
                sr.volunteerRating=Rating.objects.get(ratingNumber=request.POST.get('volunteer_rating')) 
                if UserRatings.objects.filter(user = User.objects.get(username=sr.requestor.username)).exists():
                    user = UserRatings.objects.get(user=User.objects.get(username=sr.requestor.username))
                else:
                    user = UserRatings.objects.create(user=User.objects.get(username=sr.requestor.username))
                user.ratingNumber+=int(request.POST.get('volunteer_rating'))
                user.ratingCount+=1
                user.save()
        sr.save()
        response_data['message'] = 200
    except Exception as e:
        print(e)
        response_data['message'] = 400

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def volunteer_profile_submit(request):
    response_data={}
    try:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        landmark = request.POST.get('landmark')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        pno = request.POST.get('pno')
        sno = request.POST.get('sno')
        health_related = request.POST.get('health_related')
        daily_needs = request.POST.get('daily_needs')
        information_guidance = request.POST.get('information_guidance')
        psychological_support = request.POST.get('psychological_support')
        user = User.objects.get(id = request.user.id)
        user.first_name = fname
        user.last_name = lname
        user.save()
        if UserContactInfo.objects.filter(user = user).exists():
            uc = UserContactInfo.objects.get(user = user)
            uc.address1 = address
            uc.LandMark = landmark
            uc.city = city
            uc.state = state
            uc.pincode = pincode
            uc.primaryPhoneNumber = pno
            uc.alternatePhoneNumber = sno
            uc.save()
        else:
            UserContactInfo.objects.create(user=user,address1 = address,LandMark = landmark,city = city,state = state,pincode = pincode,primaryPhoneNumber = pno,alternatePhoneNumber = sno)
        
        if health_related=='true':
            for i in ServiceSubCategory.objects.filter(serviceCategory__serviceName='Health'):
                VolunteerInterest.objects.update_or_create(volunteer=request.user,interest=i,defaults={'interest':i})
        if daily_needs=='true':
            for i in ServiceSubCategory.objects.filter(serviceCategory__serviceName='Daily Needs'):
                VolunteerInterest.objects.update_or_create(volunteer=request.user,interest=i,defaults={'interest':i})
        if information_guidance=='true':
            for i in ServiceSubCategory.objects.filter(serviceCategory__serviceName='Information Guidance'):
                VolunteerInterest.objects.update_or_create(volunteer=request.user,interest=i,defaults={'interest':i})
        if psychological_support=='true':
            for i in ServiceSubCategory.objects.filter(serviceCategory__serviceName='Psychological Support'):
                VolunteerInterest.objects.update_or_create(volunteer=request.user,interest=i,defaults={'interest':i})
        response_data['message'] = 200
    
    except Exception as e:
        print(e)
        response_data['message'] = 400
    return HttpResponse(json.dumps(response_data), content_type="application/json")
