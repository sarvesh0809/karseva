from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest,RequestStatus
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
    
        
    context={

    }
    return render(request, 'dashboard/dashboard.html', context)

