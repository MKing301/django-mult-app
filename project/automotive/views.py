from django.shortcuts import render
from .models import Service


def index(request):
    return render(
        request=request,
        template_name="automotive/index.html"
    )


def log(request):
    services = Service.objects.order_by('-service_date')
    return render(
        request=request,
        template_name="automotive/log.html",
        context={'services': services}
    )
