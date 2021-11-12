from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'task_date',
            'name',
            'vendor',
            'vendor_rep',
            'contact_num',
            'documentation',
            'cost',
            'notes',
        ]

    def clean_vendor(self):
        vendor = self.cleaned_data.get('vendor')
        if vendor is None:
            raise forms.ValidationError(
                'Please select a vendor from the dropdown!'
            )
        return vendor

    def save(self, commit=True):
        task = super(TaskForm, self).save(commit=False)
        task_date = self.cleaned_data['task_date']
        name = self.cleaned_data['name']
        vendor = self.cleaned_data['vendor']
        vendor_rep = self.cleaned_data['vendor_rep']
        contact_num = self.cleaned_data['contact_num']
        documentation = self.cleaned_data['documentation']
        cost = self.cleaned_data['cost']
        notes = self.cleaned_data['notes']
        if commit:
            task.save()
            return task
