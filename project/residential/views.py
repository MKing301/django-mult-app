from django.shortcuts import render, redirect
from .models import Task, Vendor
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator


def index(request):
    return render(
        request=request,
        template_name="residential/index.html"
    )


def add_task(request):

    vendors = Vendor.objects.order_by('name')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task saved successfully!')
            return redirect('residential:task_log')

        else:
            messages.error(request, 'An error occurred!')
            return redirect('residential:add_task')

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
