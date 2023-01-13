from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest,UserContactInfo
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