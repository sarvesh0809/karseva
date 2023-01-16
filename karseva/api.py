from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .models import ServiceSubCategory,VolunteerInterest,User,ServiceRequest
from .searializer import ServiceSubCategory_searializer,VolunteerCategory_searializer

@login_required(login_url='/index')
@api_view(['GET'])
def category_data_api(request):
    
    try:
        category = ServiceSubCategory.objects.all().order_by('-id')
        serializer = ServiceSubCategory_searializer(category,many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        pass


@login_required(login_url='/index')
@api_view(['GET'])
def volunteer_category(request,pk):
    try:
        users = User.objects.filter(volunteerinterest__interest__subCategoryName=pk)
        serializer = VolunteerCategory_searializer(users,many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        pass

