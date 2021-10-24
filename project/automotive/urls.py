from django.urls import path
from . import views


app_name = "automotive"

urlpatterns = [
    path('', views.index, name="index"),
    path('log/', views.log, name="log"),
    path('add_service/', views.add_service, name="add_service"),
    path(
        'log/edit_service/<int:id>/',
        views.edit_service,
        name="edit_service"
    ),
]
