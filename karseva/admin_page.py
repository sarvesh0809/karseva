from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserContactInfo

@login_required(login_url='login')
def adminprofile(request):
    context={

    }
    return render(request, 'admin/adminprofile.html', context)

# view pages
@login_required(login_url='login')
def All_Users(request):
    data = UserContactInfo.objects.all()
    context={
        'data':data
    }
    return render(request, 'admin/All_Users.html', context)

@login_required(login_url='login')
def ALL_Volunteers(request):
    context={

    }
    return render(request, 'admin/ALL_Volunteers.html', context)

@login_required(login_url='login')
def Complaints(request):
    context={

    }
    return render(request, 'admin/Complaints.html', context)

@login_required(login_url='login')
def Feedback(request):
    context={

    }
    return render(request, 'admin/Feedback.html', context)

@login_required(login_url='login')
def Service_Requests(request):
    context={

    }
    return render(request, 'admin/Service_Requests.html', context)

# add pages
@login_required(login_url='login')
def add_service_category(request):
    context={

    }
    return render(request, 'admin/add_service_category.html', context)

@login_required(login_url='login')
def add_service_sub_category(request):
    context={

    }
    return render(request, 'admin/add_service_sub_category.html', context)