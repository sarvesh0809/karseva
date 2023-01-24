from django.contrib import admin
from .models import * 
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserTypeInline(admin.StackedInline):
    model = UserType
    can_delete = False
    verbose_name_plural = "UserType"

class CustomUserContactInfoInline(admin.StackedInline):
    model = UserContactInfo
    can_delete = False
    verbose_name_plural = "UserContactInfo"

class CustomUserRatingsInline(admin.StackedInline):
    model = UserRatings
    can_delete = False
    verbose_name_plural = "UserRatings"

class CustomizedUserAdmin (UserAdmin):
    inlines = (CustomUserTypeInline,CustomUserContactInfoInline,CustomUserRatingsInline)


admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)
admin.site.register(ServiceCategory)
admin.site.register(RequestStatus)
admin.site.register(ServiceSubCategory)
admin.site.register(Rating)
admin.site.register(ServiceRequest)
admin.site.register(VolunteerInterest)
admin.site.register(TaskCoordinatorPincode)
admin.site.register(TaskOtp)
# admin.site.register(UserRatings)
