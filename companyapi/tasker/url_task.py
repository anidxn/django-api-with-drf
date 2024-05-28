from django.urls import path,include
from . import views

urlpatterns = [
    path("hello/", views.get_name),
    path("home/", views.home),
    path("post_task/", views.post_task),
    path("gettask/", views.get_task),
    path("patch_task/", views.patch_task),
    # ------------ view class --------------------
    path("tasks/", views.TaskView.as_view()),   # call all the http methods with this single path

    # -------- product view class ------------
    path('products/', views.ProductSearchView.as_view(), name='product-search'),   
    # TEST URL: http://localhost:8085/api/tasker/products/?search=your_search_term
]
