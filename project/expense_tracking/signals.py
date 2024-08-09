import logging

from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib import messages


logger = logging.getLogger('expense_tracking')


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    messages.success(request, "Logged in successfully!")


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    messages.success(request, "You have successfully logged out!")

