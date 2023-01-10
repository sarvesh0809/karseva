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

class CustomizedUserAdmin (UserAdmin):
    inlines = (CustomUserTypeInline,CustomUserContactInfoInline)

admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)
