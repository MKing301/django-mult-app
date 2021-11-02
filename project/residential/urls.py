from django.urls import path
from . import views


app_name = "residential"

urlpatterns = [
    path('', views.index, name="index"),
    path('task_log/', views.task_log, name="task_log"),
    path('add_task/', views.add_task, name="add_task"),
    path(
        'task_log/edit_task/<int:id>/',
        views.edit_task,
        name="edit_task"
    ),
    path('export_to_excel/', views.export_to_excel, name="export_to_excel"),
]
