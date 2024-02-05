from django.urls import path,include
from . import views

urlpatterns = [
    path("hello/", views.get_name),
    path("home/", views.home),
    path("post_task/", views.post_task),
]
