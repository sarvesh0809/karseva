from .views import index
from django.urls import path

urlpatterns = [
    # index
    path('index/',index, name='dashboard-index'),

]