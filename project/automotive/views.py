import datetime

from django.shortcuts import render, redirect
from .models import Service, Vehicle, Dealership, Advisor
from .forms import ServiceForm
from django.contrib import messages
from django.core.paginator import Paginator
from excel_response import ExcelResponse


def index(request):
    return render(
        request=request,
        template_name="automotive/index.html"
    )


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
