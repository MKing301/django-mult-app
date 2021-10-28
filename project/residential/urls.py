from django.urls import path
from . import views


app_name = "residential"

urlpatterns = [
    path('', views.index, name="index"),
    path('task_log/', views.task_log, name="task_log"),
    path('add_task/', views.add_task, name="add_task"),
]
