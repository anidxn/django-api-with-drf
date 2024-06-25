
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_page),
    path("api/v1/", include('api.url_api')),
    path("api/tasker/", include('tasker.url_task')),
    path("api/auth/", include('accounts.url_auth'))
]
