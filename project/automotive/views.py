from django.shortcuts import render
from .models import Service
from django.core.paginator import Paginator


def index(request):
    return render(
        request=request,
        template_name="automotive/index.html"
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
