from django.urls import path, include, reverse_lazy
from . import views
from rest_framework import routers
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView)


router = routers.DefaultRouter()
router.register('expense_types', views.ExpenseTypeView)

app_name = "expense_tracking"

urlpatterns = [
    path('', views.index, name="index"),
    path('expenses', views.expenses, name="expenses"),
    path('add/', views.add_expense, name="add_expense"),
    path('edit/<int:id>', views.edit_expense, name="edit_expense"),
    path("filter/<int:id>/", views.filter, name='filter'),
    path(
        "get_data/",
        views.get_data,
        name='get_data'
    ),
    path('budget', views.budget, name="budget"),
    path(
        "results/",
        views.results,
        name='results'
    ),
    path(
        "delete_expense/<int:id>",
        views.delete_expense,
        name='delete_expense'
    ),
    path("accounts/login/", views.login_request, name="login_request"),
    path("accounts/logout/", views.logout_request, name="logout_request"),
    path('api/v1/', include(router.urls)),
    path(
        "accounts/password-reset/",
        PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            success_url=reverse_lazy('expense_tracking:password_reset_done')
        ),
        name='password_reset'
    ),
    path(
        "accounts/password-reset/done/",
        PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ),
        name='password_reset_done'),
    path(
        "accounts/password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url=reverse_lazy(
                'expense_tracking:password_reset_complete'
            )
        ),
        name='password_reset_confirm'),
    path(
        "accounts/password-reset-complete/",
        PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ),
        name='password_reset_complete'),
]
