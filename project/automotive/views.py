import datetime
import logging

from django.shortcuts import render, redirect
from .models import Service, Vehicle, Dealership, Advisor
from .forms import ServiceForm
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
from django.contrib.auth.views import logout_then_login


logger = logging.getLogger(__name__)


def index(request):
    return render(
        request=request,
        template_name="automotive/index.html"
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
                return redirect("automotive:log")

            elif User.objects.filter(
                    username=form.cleaned_data.get('username')).exists():
                user = User.objects.filter(
                    username=form.cleaned_data.get('username')).values()
                if(user[0]['is_active'] is False):
                    messages.info(
                        request,
                        "Contact the administrator to activate your account!"
                    )
                    return redirect("automotive:login_request")

                else:
                    messages.error(request, 'Something went wrong!')
                    return render(
                        request=request,
                        template_name="automotive/login_automotive.html",
                        context={"form": form}
                    )

            else:
                messages.error(request, 'Something went wrong!')
                return render(
                    request=request,
                    template_name="automotive/login_automotive.html",
                    context={"form": form}
                )
        else:
            form = AuthenticationForm()
            return render(
                request=request,
                template_name="automotive/login_automotive.html",
                context={"form": form}
            )
    else:
        messages.info(
            request,
            '''You are already logged in.  You must log out to log in as
            another user.'''
        )
        return redirect("automotive:index")


@login_required
def add_service(request):

    vehicles = Vehicle.objects.order_by('year', 'make')
    dealerships = Dealership.objects.order_by('name')
    advisors = Advisor.objects.order_by('last_name')

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service record saved successfully!')
            return redirect('automotive:log')

        else:
            return render(
                request=request,
                template_name='automotive/add_service.html',
                context={
                    'form': form
                }
            )

    else:
        form = ServiceForm()

    return render(
        request=request,
        template_name='automotive/add_service.html',
        context={
            'form': form,
            'vehicles': vehicles,
            'dealerships': dealerships,
            'advisors': advisors
        }
    )


@login_required
def edit_service(request, id):
    service = Service.objects.get(id=id)

    vehicles = Vehicle.objects.exclude(
        id=service.make.pk).order_by('year', 'make')
    dealerships = Dealership.objects.exclude(
        id=service.dealership.pk).order_by('name')
    advisors = Advisor.objects.exclude(
        id=service.service_advisor.pk).order_by('last_name')

    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your service record was updted successfully!'
            )
            return redirect('automotive:log')

    else:
        form = ServiceForm(instance=service)

        return render(
            request=request,
            template_name='automotive/edit_service.html',
            context={
                'form': form,
                'service': service,
                'vehicles': vehicles,
                'dealerships': dealerships,
                'advisors': advisors
            }
        )


@login_required
def vehicle_filter(request, id):
    # Set up pagination
    p = Paginator(
        Service.objects.filter(make_id=id).order_by('-service_date'),
        10
    )
    page = request.GET.get('page')
    services = p.get_page(page)

    vehicles = Vehicle.objects.all()

    return render(
        request=request,
        template_name="automotive/log.html",
        context={
            'services': services,
            'vehicles': vehicles
        }
    )


@login_required
def log(request):
    # Set up pagination
    p = Paginator(Service.objects.order_by('-service_date'), 10)
    page = request.GET.get('page')
    services = p.get_page(page)

    vehicles = Vehicle.objects.all()

    return render(
        request=request,
        template_name="automotive/log.html",
        context={
            'services': services,
            'vehicles': vehicles
        }
    )


@login_required
def export_to_excel(request):
    services = Service.objects.all().values(
        'id',
        'service_date',
        'link',
        'make__year',
        'make__make',
        'make__model',
        'dealership__name',
        'work_performed',
        'service_advisor__first_name',
        'service_advisor__last_name',
        'mileage',
        'cost',
        'comments'
    )
    file_date_str = datetime.datetime.now().strftime('%Y%m%d')
    return ExcelResponse(
        data=services,
        output_filename=f'services_{file_date_str}',
        worksheet_name="services"
    )


@login_required
def logout_request(request):
    logger.info(f'{request.user} logged out.')
    logout(request)
    messages.success(request, 'You were successfully logged out.')
    return redirect('automotive:index')
