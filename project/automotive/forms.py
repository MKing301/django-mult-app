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

    def clean_make(self):
        make = self.cleaned_data.get('make')
        if make is None:
            raise forms.ValidationError(
                'Please select a make from the dropdown!'
            )
        return make

    def clean_dealership(self):
        dealership = self.cleaned_data.get('dealership')
        if dealership is None:
            raise forms.ValidationError(
                'Please select a dealership from the dropdown!'
            )
        return dealership

    def clean_service_advisor(self):
        service_advisor = self.cleaned_data.get('service_advisor')
        if service_advisor is None:
            raise forms.ValidationError(
                'Please select a service advisor from the dropdown!'
            )
        return service_advisor

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
