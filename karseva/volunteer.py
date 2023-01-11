from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def user_requests(request):
    context={

    }
    return render(request, 'volunteer/requests.html', context)

@login_required(login_url='login')
def volunteer_view_page(request):
    context={

    }
    return render(request, 'volunteer/volunteer_view_page.html', context)