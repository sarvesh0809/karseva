from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def task_profile(request):
    context={

    }
    return render(request, 'taskcoordinator/task_profile.html', context)

