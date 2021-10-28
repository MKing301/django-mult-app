from django.shortcuts import render
from .models import Task
from django.core.paginator import Paginator


def index(request):
    return render(
        request=request,
        template_name="residential/index.html"
    )


def task_log(request):
    # Set up pagination
    p = Paginator(Task.objects.order_by('-task_date'), 5)
    page = request.GET.get('page')
    tasks = p.get_page(page)

    return render(
        request=request,
        template_name="residential/task_log.html",
        context={'tasks': tasks}
    )
