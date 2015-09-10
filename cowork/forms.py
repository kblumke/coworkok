from django import forms
from cowork.models import *


class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'vat_id', 'website', 'company_logo', 'description' )
        labels = {
            'name': 'Company name',
            'vat_id': 'Vat ID',
            'website': 'Website',
            'company_logo': 'Company logo',
            'description': 'Company description'
        }


class LocationCreationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('country', 'city', 'address_line_1', 'address_line_2', 'address_line_3', 'postal_code', 'total_desks',
        		 'reserved_desks', 'price', )
