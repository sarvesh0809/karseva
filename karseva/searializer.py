from rest_framework import serializers
from .models import ServiceSubCategory,User,UserRatings,ServiceRequest,RequestStatus,Rating,UserContactInfo,TaskOtp

class ServiceSubCategory_searializer(serializers.ModelSerializer):
    serviceCategory = serializers.CharField(source='serviceCategory.serviceName')
    class Meta:
        model = ServiceSubCategory
        fields='__all__'

class Rating_searializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields='__all__'

class VolunteerCategory_searializer(serializers.ModelSerializer):
    try:
        phone_number = serializers.SerializerMethodField()
        ratings = serializers.SerializerMethodField()
        def get_phone_number(self, obj):
            return obj.usercontactinfo.primaryPhoneNumber
        def get_ratings(self, obj):
            rating = UserRatings.objects.get(user__username = obj.username)
            if rating:
                return rating.ratingNumber/rating.ratingCount
            else:
                return 0
        class Meta:
            model = User
            fields=['id','username','phone_number','ratings','is_active']
    except Exception as e:
        print(e)

class RequestStatusSearializer(serializers.ModelSerializer):
    class Meta:
        model = RequestStatus
        fields= ['statusName']

class UserContactInfoSearializer(serializers.ModelSerializer):
    class Meta:
        model = UserContactInfo
        fields= '__all__'

class UserSearializer(serializers.ModelSerializer):
    usercontactinfo = UserContactInfoSearializer()
    primaryphonenumber  = serializers.CharField(source='usercontactinfo.primaryPhoneNumber')
    class Meta:
        model = User
        fields= '__all__'

class ServiceSubCategorySearializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSubCategory
        fields=['subCategoryName']

class TaskOtpSearializer(serializers.ModelSerializer):
    class Meta:
        model = TaskOtp
        fields='__all__'

class ServiceRequest_searializer(serializers.ModelSerializer): # keep particular's fields only - 16/01/23
    volunteer = UserSearializer()
    requestor = UserSearializer()
    requestStatus = RequestStatusSearializer()
    userRating = Rating_searializer()
    volunteerRating = Rating_searializer()
    subCategory = ServiceSubCategorySearializer()
    taskOtp = TaskOtpSearializer(source='taskotp')
    requestCreatedOn = serializers.DateTimeField(format="%b %d, %Y %H:%M")
    # requestCreatedon = serializers.DateTimeField(format="%b %d, %Y %H:%M")
    requestTimeInBound= serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    requestTimeOutBound= serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    actualTimeInBound= serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    actualTimeOutBound= serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    class Meta:
        model = ServiceRequest
        fields='__all__'