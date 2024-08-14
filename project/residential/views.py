import datetime
import logging

from django.shortcuts import render, redirect
from .models import Task, Vendor
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from excel_response import ExcelResponse
from django.contrib.auth.models import User
from django.contrib.auth import (
    login, logout, authenticate, update_session_auth_hash
)
from django.contrib.auth.decorators import login_required
# from .signals import log_user_logout
from django.contrib.auth.forms import AuthenticationForm
from .signals import log_user_logout
from django.contrib.auth.views import logout_then_login


logger = logging.getLogger('residential')


def index(request):
    return render(
        request=request,
        template_name="residential/index.html"
    )


def login_request(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(
                    request,
                    f'{username} logged in successfully.'
                )
                logger.info(f'{request.user} logged in successfully.')
                return redirect("residential:task_log")

            elif User.objects.filter(
                    username=form.cleaned_data.get('username')).exists():
                user = User.objects.filter(
                    username=form.cleaned_data.get('username')).values()
                if(user[0]['is_active'] is False):
                    messages.info(
                        request,
                        "Contact the administrator to activate your account!"
                    )
                    return redirect("residential:login_request")

                else:
                    messages.error(request, 'Something went wrong!')
                    return render(
                        request=request,
                        template_name="residential/login_residential.html",
                        context={"form": form}
                    )

            else:
                messages.error(request, 'Something went wrong!')
                return render(
                    request=request,
                    template_name="residential/login_residential.html",
                    context={"form": form}
                )
        else:
            form = AuthenticationForm()
            return render(
                request=request,
                template_name="residential/login_residential.html",
                context={"form": form}
            )
    else:
        messages.info(
            request,
            '''You are already logged in.  You must log out to log in as
            another user.'''
        )
        return redirect("residential:index")


@login_required
def add_task(request):

    vendors = Vendor.objects.order_by('name')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task saved successfully!')
            return redirect('residential:task_log')

        else:
            return render(
                request=request,
                template_name='residential/add_task.html',
                context={
                    'form': form,
                    'vendors': vendors
                }
            )

    else:
        form = TaskForm()

    return render(
        request=request,
        template_name='residential/add_task.html',
        context={
            'form': form,
            'vendors': vendors
        }
    )


@login_required
def edit_task(request, id):
    task = Task.objects.get(id=id)

    vendors = Vendor.objects.exclude(
        id=task.pk).order_by('name')

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your task record was updted successfully!'
            )
            return redirect('residential:task_log')

    else:
        form = TaskForm(instance=task)

        return render(
            request=request,
            template_name='residential/edit_task.html',
            context={
                'form': form,
                'task': task,
                'vendors': vendors
            }
        )


@login_required
def task_log(request):
    # Set up pagination
    p = Paginator(Task.objects.order_by('-task_date'), 10)
    page = request.GET.get('page')
    tasks = p.get_page(page)

    vendors = Vendor.objects.order_by('name')

    return render(
        request=request,
        template_name="residential/task_log.html",
        context={
            'tasks': tasks,
            'vendors': vendors
        }
    )


@login_required
def filter(request, id):
    # Set up pagination
    p = Paginator(Task.objects.filter(vendor=id).order_by('-task_date'), 10)
    page = request.GET.get('page')
    tasks = p.get_page(page)

    vendors = Vendor.objects.order_by('name')

    return render(
        request=request,
        template_name="residential/task_log.html",
        context={
            'tasks': tasks,
            'vendors': vendors
        }
    )


@login_required
def export_to_excel(request):
    tasks = Task.objects.all().values(
        'id',
        'task_date',
        'name',
        'vendor__name',
        'vendor_rep',
        'contact_num',
        'documentation',
        'cost',
        'notes'
    )

    file_date_str = datetime.datetime.now().strftime('%Y%m%d')
    return ExcelResponse(
        data=tasks,
        output_filename=f'tasks_{file_date_str}',
        worksheet_name="tasks"
    )


@login_required
def logout_request(request):
    logout(request)
    logger.info('You were successfully logged out.')
    return redirect('residential:index')
