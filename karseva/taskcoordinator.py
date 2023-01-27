from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import TaskCoordinatorPincode,ServiceRequest
from .searializer import ServiceRequest_searializer
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
    context={
        "request_data":request_data
    }
    return render(request, 'taskcoordinator/task_view_page.html', context)

@login_required(login_url='login')
def task_all_requests(request):
    context={
        'services':ServiceRequest.objects.filter(pincode__in=list(TaskCoordinatorPincode.objects.filter(coordinator=request.user).values_list('pincode',flat=True))).order_by("-id")
    }
    return render(request, 'taskcoordinator/task_all_requests.html', context)