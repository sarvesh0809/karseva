from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest,RequestStatus,User
# Create your views here.
# @login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")
    context={

    }
    return render(request, 'index/index.html', context)


def user_login(request):
    return render(request, 'index/index.html',)


@login_required(login_url='login')
def dashboard(request):
    volunteers = User.objects.filter(usertype__user_type='VOLUNTEER').count()
    users = User.objects.filter(usertype__user_type='USER').count()
    services = ServiceRequest.objects.all().count()
    coordinator =  User.objects.filter(usertype__user_type='TASK COORDINATOR').count()
    print(coordinator)
    
    context={
        'volunteers':volunteers,'users':users,'services':services,'coordinator':coordinator
    }
    return render(request, 'dashboard/dashboard.html', context)

