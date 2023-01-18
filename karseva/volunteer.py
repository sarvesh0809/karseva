from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest,UserContactInfo,RequestStatus,Rating,User,UserRatings
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
