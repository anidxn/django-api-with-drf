from django.urls import path, include
from . import views
#--- import for router -----
from rest_framework import routers

# add a router
rt = routers.DefaultRouter()
# register the viewset with this router
rt.register(r'companies', views.CompanyViewSet)
rt.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('', include(rt.urls))
]


# companies/{company_id}/employees