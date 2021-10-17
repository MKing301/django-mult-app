from django.shortcuts import render, redirect
from .models import Service, Vehicle, Dealership, Advisor
from .forms import ServiceForm
from django.contrib import messages
from django.core.paginator import Paginator


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
            messages.error(request, 'An error occurred!')
            return redirect('automotive:add_service')

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


def log(request):
    # Set up pagination
    p = Paginator(Service.objects.order_by('-service_date'), 5)
    page = request.GET.get('page')
    services = p.get_page(page)

    return render(
        request=request,
        template_name="automotive/log.html",
        context={'services': services}
    )
