from django.urls import path, include
from . import views

urlpatterns = [
    path('getdata/', views.get_api_data, name='get-data'),
    path('home/', views.home, name='home'),
    path('', views.home),
]