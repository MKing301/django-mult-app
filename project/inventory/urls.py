from django.urls import path, reverse_lazy
from . import views


app_name = "inventory"

urlpatterns = [
    path("", views.index, name="index"),
    path("inventory/summary", views.summary, name="summary"),
    path("inventory/inventory", views.inventory, name="inventory"),
    path("inventory/add_item", views.add_item, name="add_item"),
    path("inventory/edit_item/<int:id>", views.edit_item, name="edit_item"),
    path("inventory/load_areas", views.load_areas, name="load_areas"),
    path("inventory/notes/<int:id>", views.notes, name="notes"),
    path(
        "inventory/export_to_excel", views.export_to_excel, name="export_to_excel"
    ),
    path("accounts/logout/", views.logout_request, name="logout_request"),
    path("accounts/login/", views.login_request, name="login_request"),
    path('maintenance/', views.maintenance, name='maintenance'),
]
