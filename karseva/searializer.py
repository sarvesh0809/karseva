from rest_framework import serializers
from .models import ServiceSubCategory,User,UserRatings

class ServiceSubCategory_searializer(serializers.ModelSerializer):
    serviceCategory = serializers.CharField(source='serviceCategory.serviceName')
    class Meta:
        model = ServiceSubCategory
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
            fields=['username','phone_number','ratings','is_active']
    except Exception as e:
        print(e)