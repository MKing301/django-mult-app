import datetime

from django.shortcuts import render, redirect
from .models import Task, Vendor
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from excel_response import ExcelResponse


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
