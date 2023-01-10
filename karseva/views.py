from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required(login_url='login')
def index(request):
    context={

    }
    return render(request, 'index/index.html', context)


def user_login(request):
    return render(request, 'user/login.html',)


@login_required(login_url='login')
def dashboard(request):
    context={

    }
    return render(request, 'dashboard/dashboard.html', context)
