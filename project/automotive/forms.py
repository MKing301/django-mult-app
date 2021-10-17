from django import forms
from .models import Service
from datetime import datetime


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'service_date',
            'link',
            'make',
            'dealership',
            'work_performed',
            'service_advisor',
            'mileage',
            'cost',
            'comments',
        ]

        readonly_fields = [
            'inserted_date'
        ]

    def save(self, commit=True):
        service = super(ServiceForm, self).save(commit=False)
        service_date = self.cleaned_data['service_date']
        link = self.cleaned_data['link']
        make = self.cleaned_data['make']
        dealership = self.cleaned_data['dealership']
        work_performed = self.cleaned_data['work_performed']
        service_advisor = self.cleaned_data['service_advisor']
        mileage = self.cleaned_data['mileage']
        cost = self.cleaned_data['cost']
        comments = self.cleaned_data['comments']
        inserted_date = datetime.now()
        if commit:
            service.save()
            return service
