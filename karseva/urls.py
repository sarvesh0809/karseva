from . import accounts,users,views,volunteer,api,admin_page,taskcoordinator
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

    # admin
    # path('adminprofile',admin_page.adminprofile, name='adminprofile'),
    path('All_Users',admin_page.All_Users, name='All_Users'),
    path('All_user_id/<int:pk>/',admin_page.All_user_id, name='All_user_id'),
    path('All_volunteer_id/<int:pk>/',admin_page.All_volunteer_id, name='All_volunteer_id'),
    path('ALL_Volunteers',admin_page.ALL_Volunteers, name='ALL_Volunteers'),
    path('user_profile_edit',admin_page.user_profile_edit, name='user_profile_edit'),
    path('volunteer_profile_edit',admin_page.volunteer_profile_edit, name='volunteer_profile_edit'),
    path('Complaints',admin_page.Complaints, name='Complaints'),
    path('Feedback',admin_page.Feedback, name='Feedback'),
    path('Service_Requests',admin_page.Service_Requests, name='Service_Requests'),
    path('add_service_sub_category',admin_page.add_service_sub_category, name='add_service_sub_category'),
    path('add_service_category',admin_page.add_service_category, name='add_service_category'),
    
    # task coordinator
    path('task_profile',taskcoordinator.task_profile, name='task_profile'),
    path('task_all_requests',taskcoordinator.task_all_requests, name='task_all_requests'),
    path('task_all_requests/<int:pk>/',taskcoordinator.task_view_page, name='task_view_page'),
    path('task_edit_submit',taskcoordinator.task_edit_submit, name='task_edit_submit'),
    path('task_complaints',taskcoordinator.task_complaints, name='task_complaints'),

    #volunteer
    path('volunteerprofile',volunteer.volunteerprofile, name='volunteerprofile'),
    path('volunteer_profile_submit',volunteer.volunteer_profile_submit, name='volunteer_profile_submit'),
    path('user_requests',volunteer.user_requests, name='user_requests'),
    path('volunteer_view_page',volunteer.volunteer_view_page, name='volunteer_view_page'),
    path('load_volunteer_data/<int:pk>/',volunteer.load_volunteer_data, name='load_volunteer_data'),
    path('view_user_request_volunteer/<int:pk>/',volunteer.view_user_request_volunteer, name='view_user_request_volunteer'),
    path('user_requests/view/<int:pk>/',volunteer.user_requests_view_all, name='user_requests_view_all'),
    path('volunteer_procure_submit',volunteer.volunteer_procure_submit, name='volunteer_procure_submit'),
    path('volunteer_view_request_submit/<int:pk>',volunteer.volunteer_view_request_submit, name='volunteer_view_request_submit'),
    path('volunterr_otp_submit',volunteer.volunterr_otp_submit, name='volunterr_otp_submit'),

    # user
    path('userprofile',users.userprofile, name='userprofile'),
    path('user_profile_submit',users.user_profile_submit, name='user_profile_submit'),
    path('submit_new_request',users.submit_new_request, name='submit_new_request'),
    path('user_request_submit',users.user_request_submit, name='user_request_submit'),
    path('load_request_data/<int:pk>/',users.load_request_data, name='load_request_data'),
    path('view_user_request/<int:pk>/',users.view_user_request, name='view_user_request'),
    path('user_view_request_submit/<int:pk>',users.user_view_request_submit, name='user_view_request_submit'),



    #api
    path('category_data_api',api.category_data_api, name='category_data_api'),
    path('volunteer/category/<str:pk>/',api.volunteer_category, name='volunteer_category'),
    path('volunteerName_category',api.volunteerName_category, name='volunteerName_category'),



]