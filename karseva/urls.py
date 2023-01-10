from . import accounts,users,views
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # index
    path('index/',views.index, name='index'),

    # Account 
    path('login/',views.user_login, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('userSignup/',accounts.userSignup, name='userSignup'),
    path('userLogin/',accounts.userLogin, name='userLogin'),
    path('checkEmail/',accounts.checkEmail, name='checkEmail'),

    # Auth
    path("accounts/", include("allauth.urls")), #most important


    #dashboard
    path('dashboard',views.dashboard, name='dashboard'),


]