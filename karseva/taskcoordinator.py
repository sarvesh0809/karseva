from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import TaskCoordinatorPincode,ServiceRequest,User,RequestStatus,TaskActivity
from .searializer import ServiceRequest_searializer
import json
@login_required(login_url='login')
def task_profile(request):
    context={
          }
    return render(request, 'taskcoordinator/task_profile.html', context)

@login_required(login_url='login')
def task_complaints(request):
    services = ServiceRequest.objects.all()
    context={
        "services":services
    }
    return render(request, 'taskcoordinator/task_complaints.html', context)

@login_required(login_url='login')
def task_view_page(request,pk):
    services = ServiceRequest.objects.get(id=pk)
    request_data = ServiceRequest_searializer(services,many=False)
    task_activity = TaskActivity.objects.filter(service_request = services).order_by('-id')

    context={
        "request_data":request_data,
        "task_activity":task_activity
    }
    return render(request, 'taskcoordinator/task_view_page.html', context)

@login_required(login_url='login')
def task_all_requests(request):
    task = ServiceRequest.objects.filter(pincode__in=list(TaskCoordinatorPincode.objects.filter(coordinator=request.user).values_list('pincode',flat=True))).count()
  
    context={
        'services':ServiceRequest.objects.filter(pincode__in=list(TaskCoordinatorPincode.objects.filter(coordinator=request.user).values_list('pincode',flat=True))).order_by("-id"),
        'task': task
    }
    return render(request, 'taskcoordinator/task_all_requests.html', context)


@login_required(login_url='login')
def task_edit_submit(request):
    response_data={}
    try:
        volunteer = request.POST.get('volunteerName')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        description = request.POST.get('description')
        status = request.POST.get('status')
        time_in = request.POST.get('time_in')
        time_out = request.POST.get('time_out')
        task_id = request.POST.get('task_id')
        sr = ServiceRequest.objects.get(id=task_id)
        sr.address = address
        sr.pincode = pincode
        sr.description = description
        sr.requestStatus = RequestStatus.objects.get(statusName=status)
        if sr.volunteer.username != volunteer:
            sr.volunteer = User.objects.get(username=volunteer)
        if time_in != sr.requestTimeInBound and time_in != '' or time_in == 'undefined':
            sr.requestTimeInBound =time_in
        if time_out != sr.requestTimeOutBound and time_out != '' or time_out == 'undefined':
            sr.requestTimeOutBound =time_out
        sr.save()
        response_data['message'] = 200

    except Exception as e:
        print(e)
        response_data['message'] = 400

    return HttpResponse(json.dumps(response_data), content_type="application/json")
        