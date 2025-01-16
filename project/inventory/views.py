import logging
import csv
import datetime
import pandas as pd
import plotly.graph_objs as go

from pytz import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import (
    login, logout, authenticate, update_session_auth_hash
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import (
    InventoryItem,
    ItemNotes,
    ItemStatus,
    Area,
    MapLocation,
    Manufacturer,
    Assignee,
    ApprovalList
)
from .forms import (
    NoteForm,
    InventoryForm
)
from django.urls import reverse_lazy
from plotly.offline import plot
from pretty_html_table import build_table


logger = logging.getLogger(__name__)
EST = timezone('US/Eastern')


def maintenance(request):
    return render(
        request=request,
        template_name='inventory/maintenance.html')


def index(request):
    return render(request=request,
                  template_name="inventory/index.html"
                  )


@login_required
def summary(request):

    try:
        # Create dataframe from all records for specified fields
        df = pd.DataFrame(list(
            InventoryItem.objects.all().values(
                'item_location__name',
                'qty',
                'total_cost'
            )
        )
        )

        if len(df.index) == 0:
            return render(
                request=request,
                template_name='inventory/summary.html',
                context={
                    'msg': 'No records found!'
                }
            )
        else:
            #grouped_df = df.groupby(
            #    'item_location__name', as_index=False
            #    ).sum()

            grouped_df = df.groupby(
                ['item_location__name']
                ).agg({'qty': 'sum', 'total_cost': 'sum'}).reset_index()

            grouped_df.columns = [
                'Location', 'Total Number of Items', 'Total Cost'
            ]

            #grouped_df['Total Cost'] = grouped_df['Total Cost'].map(
            #    '${:,.2f}'.format)

            if len(grouped_df.index) == 0:
                return render(
                    request=request,
                    template_name='inventory/summary.html',
                    context={
                        'msg': 'No records found!'
                    }
                )
            else:

                trace_pie = go.Pie(
                    values=grouped_df['Total Number of Items'],
                    labels=grouped_df['Location'],
                    # textinfo='percent+value',
                )

                config = {
                    'responsive': True,
                    'displaylogo': False
                }

                data = [trace_pie]

                fig_pie = go.Figure(data=data)

                fig_pie.update_layout(
                    autosize=True,
                    # width=600,
                    # height=600,
                    title_text='<b>Inventory Percentage per Location</b>',
                    title_x=0.50,
                    title_y=0.95,
                    title_font=dict(size=18),
                    legend_font_size=14,
                    legend=dict(
                        orientation="h"
                    ),
                    # legend_yanchor='bottom',
                    # legend_y=0,
                    # legend_xanchor='right',
                    # legend_x=2.5,
                    # margin=dict(
                    #     l=0,
                    #     r=0,
                    #     b=0,
                    #     t=0
                    # ),
                )

                plt_div_pie = plot(
                    fig_pie, config=config, output_type='div'
                )

                return render(
                    request=request,
                    template_name='inventory/summary.html',
                    context={
                        'grouped_df': build_table(
                            grouped_df,
                            'blue_dark',
                            text_align='right'
                        ),
                        'plt_div_pie': plt_div_pie
                    }
                )

    except Exception as e:
        logging.error(f'Exception on data visualization: {e}')
        return render(
                    request=request,
                    template_name='inventory/summary.html',
                    context={
                        'msg': 'No records found!'
                    }
                )

@login_required
def inventory(request):
    #inventory_list = InventoryItem.objects.all()
    inventory_list = InventoryItem.objects.all().values(
        'id',
        'asset_id',
        'name',
        'stat__name',
        'description',
        'item_location__name',
        'item_area__name',
        'mfg__name',
        'model_no',
        'serial_no',
        'qty',
        'total_cost',
        'cost_per_item',
        'assigned_to__name',
        'approved_by__name',
        'approved_date',
        'purchased_from',
        'purchase_date',
        'inserted_by',
        'inserted_date',
        'modified_by',
        'modified_date'
    ).order_by('-purchase_date')

    return render(request=request,
                  template_name="inventory/inventory.html",
                  context={
                      'inventory_list': inventory_list
                  }
                  )


@login_required
def load_areas(request):
    loc = request.GET.get('item_location')
    areas = Area.objects.filter(map_loc=loc).order_by('name')
    return render(
        request=request,
        template_name="inventory/areasOpts.html",
        context={
            'loc': loc,
            'areas': areas
        }
    )


@login_required
def add_item(request):
    stats = ItemStatus.objects.all().values().order_by('name').values()
    areas = Area.objects.all().values().order_by('name').values()
    locations = MapLocation.objects.all().values().order_by('name').values()
    mfgs = Manufacturer.objects.all().order_by('name').values()
    assignees = Assignee.objects.all().order_by('name').values()
    approvers = ApprovalList.objects.all().order_by('name').values()

    if request.method == "POST":
        form = InventoryForm(request.POST)

        if form.is_valid():

            item_to_insert = form.save(commit=False)
            item_to_insert.stat = form.cleaned_data['stat']
            item_to_insert.asset_id = form.cleaned_data['asset_id']
            item_to_insert.name = form.cleaned_data['name']
            item_to_insert.description = form.cleaned_data['description']
            item_to_insert.item_location = form.cleaned_data['item_location']
            item_to_insert.item_area = form.cleaned_data['item_area']
            item_to_insert.mfg = form.cleaned_data['mfg']
            item_to_insert.model_no = form.cleaned_data['model_no'].upper()
            if form.cleaned_data['serial_no'] is None:
                item_to_insert.serial_no = form.cleaned_data['serial_no']
            else:
                item_to_insert.serial_no = (
                    form.cleaned_data['serial_no'].upper())
            item_to_insert.qty = form.cleaned_data['qty']
            item_to_insert.total_cost = form.cleaned_data['total_cost']
            item_to_insert.cost_per_item = form.cleaned_data['total_cost']/form.cleaned_data['qty']
            item_to_insert.assigned_to = form.cleaned_data['assigned_to']
            item_to_insert.approved_by = form.cleaned_data['approved_by']
            item_to_insert.approved_date = form.cleaned_data['approved_date']
            item_to_insert.purchased_from = form.cleaned_data['purchased_from']
            item_to_insert.purchase_date = form.cleaned_data['purchase_date']
            item_to_insert.inserted_by = request.user
            item_to_insert.inserted_date = datetime.datetime.now(tz=EST)
            item_to_insert.save()
            messages.success(
                request,
                'New inventory item added successfully!'
            )

            return redirect('inventory:inventory')

        else:
            return render(
                request=request,
                template_name="inventory/add_item.html",
                context={"form": form}
            )

    else:
        form = NoteForm()
        return render(
            request=request,
            template_name="inventory/add_item.html",
            context={
                'stats': stats,
                'areas': areas,
                'locations': locations,
                'mfgs': mfgs,
                'assignees': assignees,
                'approvers': approvers
            }
        )


@login_required
def edit_item(request, id):

    # Obtain record to edit by id
    entry_to_edit = InventoryItem.objects.get(id=id)

    # Obtain list of status in order by name, except the selected value
    # by id from the form
    stat_list = ItemStatus.objects.exclude(
        id=entry_to_edit.stat.pk
    ).order_by('name')

    # Obtain list of locations in order by name, except the selected value
    # by id from the form
    loc_list = MapLocation.objects.exclude(
        id=entry_to_edit.item_location.pk
    ).order_by('name')

    # Get area
    # current_area = entry_to_edit.location.name
    # lst = (list(current_area.split(" ")))
    # cur_area = lst[0]

    # Obtain list of areas in order by name, except the selected value
    # by id from the form
    area_list = Area.objects.filter(
        map_loc=entry_to_edit.item_location.pk).order_by('name')

    # Obtain list of manufacturers in order by name, except the selected value
    # by id from the form
    mfg_list = Manufacturer.objects.exclude(
        id=entry_to_edit.mfg.pk
    ).order_by('name')

    # Obtain list of assignees in order by name, except the selected value
    # by id from the form
    assignee_list = Assignee.objects.all()

    # Obtain list of approvers in order by name, except the selected value
    # by id from the form
    approvers_list = ApprovalList.objects.all()

    if request.method == "POST":
        form = InventoryForm(request.POST, instance=entry_to_edit)
        if form.is_valid():
            entry_to_edit = form.save(commit=False)
            entry_to_edit.stat = form.cleaned_data['stat']
            entry_to_edit.asset_id = form.cleaned_data['asset_id']
            entry_to_edit.name = form.cleaned_data['name']
            entry_to_edit.description = form.cleaned_data['description']
            entry_to_edit.item_location = form.cleaned_data['item_location']
            entry_to_edit.item_area = form.cleaned_data['item_area']
            entry_to_edit.mfg = form.cleaned_data['mfg']
            entry_to_edit.model_no = form.cleaned_data['model_no'].upper()
            if form.cleaned_data['serial_no'] is None:
                entry_to_edit.serial_no = form.cleaned_data['serial_no']
            else:
                entry_to_edit.serial_no = (
                    form.cleaned_data['serial_no'].upper())
            entry_to_edit.qty = form.cleaned_data['qty']
            entry_to_edit.total_cost = form.cleaned_data['total_cost']
            entry_to_edit.cost_per_item = entry_to_edit.total_cost/entry_to_edit.qty
            entry_to_edit.assigned_to = form.cleaned_data['assigned_to']
            entry_to_edit.approved_by = form.cleaned_data['approved_by']
            entry_to_edit.approved_date = form.cleaned_data['approved_date']
            entry_to_edit.purchased_from = form.cleaned_data['purchased_from']
            entry_to_edit.purchase_date = form.cleaned_data['purchase_date']
            entry_to_edit.inserted_by = entry_to_edit.inserted_by
            entry_to_edit.inserted_date = entry_to_edit.inserted_date
            entry_to_edit.modified_by = str(request.user)
            entry_to_edit.modified_date = datetime.datetime.now(tz=EST)
            entry_to_edit.save()
            messages.success(
                request,
                'Updated successfully!'
            )
            return redirect('inventory:inventory')
        else:
            messages.error(
                    request,
                    form.errors
            )
            return redirect('inventory:inventory')

    else:
        form = InventoryForm(instance=entry_to_edit)
        return render(
            request=request,
            template_name='inventory/edit_item.html',
            context={
                'stat_list': stat_list,
                'loc_list': loc_list,
                'area_list': area_list,
                'mfg_list': mfg_list,
                'assignee_list': assignee_list,
                'approvers_list': approvers_list,
                'entry_to_edit': entry_to_edit,
                'form': form
            }
        )


@login_required
def notes(request, id):
    item = InventoryItem.objects.get(id=id)
    item_notes = ItemNotes.objects.filter(item=item)

    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():

            note_to_insert = form.save(commit=False)
            note_to_insert.item_id = id
            note_to_insert.comment = form.cleaned_data['comment']
            note_to_insert.inserted_by = request.user
            note_to_insert.inserted_date = datetime.datetime.now(tz=EST)
            note_to_insert.save()
            messages.success(
                request,
                'Note added successfully!'
            )

            return redirect('inventory:notes', id=id)

        else:
            return render(
                request=request,
                template_name="inventory/notes.html",
                context={
                    'item': item,
                    'item_notes': item_notes
                }
            )

    else:
        form = NoteForm()
        return render(
            request=request,
            template_name="inventory/notes.html",
            context={
                'item': item,
                'item_notes': item_notes
            }
        )


@login_required
def export_to_excel(request):

    try:

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="inventory.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                'ID',
                'Status',
                'Asset ID',
                'Item',
                'Description',
                'Model #',
                'Serial #',
                'Qty',
                'Total Cost',
                'Assigned To',
                'Approval Date',
                'Purchased From',
                'Purchase Date',
                'Inserted By',
                'Inserted Date',
                'Modified By',
                'Modified Date',
                'Approved By',
                'Location',
                'Area',
                'Mfg'
            ]
        )

        items = InventoryItem.objects.all().values_list(
            'id',
            'stat__name',
            'asset_id',
            'name',
            'description',
            'model_no',
            'serial_no',
            'qty',
            'total_cost',
            'assigned_to',
            'approved_date',
            'purchased_from',
            'purchase_date',
            'inserted_by',
            'inserted_date',
            'modified_by',
            'modified_date',
            'approved_by_id__name',
            'item_location_id__name',
            'item_area_id__name',
            'mfg_id__name'
        )

        for item in items:
            writer.writerow(item)
        return response

    except Exception as e:
        logger.error(f'Export failed: {e}')
        return redirect("inventory:summary")


def login_request(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                logger.info(f'{request.user} logged in.')
                return redirect("inventory:summary")

            elif User.objects.filter(
                    username=form.cleaned_data.get('username')).exists():
                user = User.objects.filter(
                    username=form.cleaned_data.get('username')).values()
                if (user[0]['is_active'] is False):
                    messages.info(
                        request,
                        "Contact the administrator to activate your account!"
                    )
                    return redirect("inventory:login_request")

                else:
                    return render(
                        request=request,
                        template_name="inventory/login_inventory.html",
                        context={"form": form}
                    )

            else:
                return render(
                    request=request,
                    template_name="inventory/login_inventory.html",
                    context={"form": form}
                )
        else:
            form = AuthenticationForm(request, data=request.POST)
            return render(
                request=request,
                template_name="inventory/login_inventory.html",
                context={"form": form}
            )
    else:
        messages.info(
            request,
            '''You are already logged in.  You must log out to log in as
            another user.'''
        )
        return redirect("inventory:index")


@login_required
def logout_request(request):
    logger.info(f'{request.user} logged out.')
    logout(request)
    return redirect('inventory:index')
