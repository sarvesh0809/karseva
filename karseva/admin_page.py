from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserContactInfo,UserType,User
from django.http import JsonResponse
import json

@login_required(login_url='login')
def adminprofile(request):
    context={

    }
    return render(request, 'admin/adminprofile.html', context)


# view pages
@login_required(login_url='login')
def All_Users(request):
    data = User.objects.filter(usertype__user_type='USER')     
    context={
        'data':data
    }
    return render(request, 'admin/All_Users.html', context)

@login_required(login_url='login')
def All_volunteer_id(request,pk):
    data = User.objects.filter(id=pk,usertype__user_type='VOLUNTEER')     
    context={
        'data':data
    }
    return render(request, 'admin/All_volunteer_id.html', context)

@login_required(login_url='login')
def All_user_id(request,pk):
    data = User.objects.filter(id=pk,usertype__user_type='USER')  
    context={
        'data':data
    }
    return render(request, 'admin/All_user_id.html', context)

@login_required(login_url='login')
def ALL_Volunteers(request):
    data = User.objects.filter(usertype__user_type='VOLUNTEER')   
    context={
        'data':data
    }
    return render(request, 'admin/ALL_Volunteers.html', context)


def user_profile_edit(request):
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
        response_data['message'] = 200
    except Exception as e:
        print(e)
        response_data['message'] = 400
    return HttpResponse(json.dumps(response_data), content_type="application/json")





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