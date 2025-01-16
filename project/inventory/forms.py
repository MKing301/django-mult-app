from django import forms
from .models import ItemNotes, InventoryItem


class InventoryForm(forms.ModelForm):

    class Meta:
        model = InventoryItem
        fields = (
            'asset_id',
            'name',
            'stat',
            'description',
            'item_location',
            'item_area',
            'mfg',
            'model_no',
            'serial_no',
            'qty',
            'total_cost',
            'cost_per_item',
            'assigned_to',
            'approved_by',
            'approved_date',
            'purchased_from',
            'purchase_date'
        )


class NoteForm(forms.ModelForm):

    class Meta:
        model = ItemNotes
        fields = (
            'comment',
        )
