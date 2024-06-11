from django.urls import path,include
from . import views

urlpatterns = [
    path("hello/", views.get_name),
    path("home/", views.home),
    # ------- using seperate view functions ----------
    path("post_task/", views.post_task),
    path("gettask/", views.get_task),
    path("task-detail/<str:pk>/", views.task_detail, name='task-detail'),
    path("update_task/", views.put_task),
    path("patch_task/", views.patch_task),
    path("task-delete/<str:pk>/", views.del_task, name='task-delete'),

    # ------------ view class --------------------
    path("tasks/", views.TaskView.as_view()),   # call all the http methods with this single path

    # ------------- Search the tasks by date range -----------------
    path('taskbydate/', views.TaskListAPIView.as_view(), name='task-list-bydate'),

    # -------- product view class ------------
    path('products/', views.ProductSearchView.as_view(), name='product-search'),   
    # TEST URL: http://localhost:8085/api/tasker/products/?search=your_search_term
]
