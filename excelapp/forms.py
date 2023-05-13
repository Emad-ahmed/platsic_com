from django import forms
from django.forms import fields, widgets
from django.core import validators
from excelapp.models import HeadCompany,SubCompany, ClientCompany


class HeadForm(forms.ModelForm):
    class Meta:
        model = HeadCompany
        fields = ('name',  'short_name', 'line1','line2','line3','line4', 'description', 'unit_price', 'image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'line1': forms.TextInput(attrs={'class': 'form-control'}),
            'line2': forms.TextInput(attrs={'class': 'form-control'}),
            'line3': forms.TextInput(attrs={'class': 'form-control'}),
            'line4': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class SubcompanyForm(forms.ModelForm):
    class Meta:
        model = SubCompany
        fields = ('head_company',  'name', 'line1', 'line2', 'line3', 'line4', 'invoicedate', 'rangemin', 'rangemax')

        widgets = {
            'head_company': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Name'}),
            'line1': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'line1'}),
            'line2': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'line2'}),
            'line3': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'line3'}),
            'line4': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'line4'}),
            'rangemin': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Min'}),
            'rangemax': forms.NumberInput(attrs={'class': 'form-control',  'placeholder' : 'Max'}),
            'invoicedate': forms.DateInput(attrs={'type' :'date',  'class': 'form-control',  'placeholder' : 'Max'}),

        }

class SubcompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = SubCompany
        fields = ('head_company',  'name', 'line1', 'line2', 'line3', 'line4', 'Invoicenumber', 'invoicedate', 'rangemin', 'rangemax')

        widgets = {
            'head_company': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Name'}),
            'line1': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'line1'}),
            'line2': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'line2'}),
            'line3': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'line3'}),
            'line4': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'line4'}),
            'rangemin': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Min'}),
            'rangemax': forms.NumberInput(attrs={'class': 'form-control',  'placeholder' : 'Max'}),
            'Invoicenumber': forms.NumberInput(attrs={'class': 'form-control',  'placeholder' : 'Max'}),
            'invoicedate': forms.DateInput(attrs={'type' :'date',  'class': 'form-control',  'placeholder' : 'Max'}),
        }

class ClientCompanyForm(forms.ModelForm):
    class Meta:
        model = ClientCompany
        fields = ('head_company',  'name', 'line1', 'line2', 'line3', 'line4', 'invoicedate', 'rangemin', 'rangemax')

        widgets = {
            'head_company': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'line1': forms.TextInput(attrs={'class': 'form-control'}),
            'line2': forms.TextInput(attrs={'class': 'form-control'}),
            'line3': forms.TextInput(attrs={'class': 'form-control'}),
            'line4': forms.TextInput(attrs={'class': 'form-control'}),
            'rangemin': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Min'}),
            'rangemax': forms.NumberInput(attrs={'class': 'form-control',  'placeholder' : 'Max'}),
            'invoicedate': forms.DateInput(attrs={'type' :'date',  'class': 'form-control',  'placeholder' : 'Max'}),
        }



class ClientcompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = ClientCompany
        fields = ('head_company',  'name', 'line1', 'line2', 'line3', 'line4', 'Invoicenumber', 'invoicedate', 'rangemin', 'rangemax')

        widgets = {
            'head_company': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Name'}),
            'line1': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'line1'}),
            'line2': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'line2'}),
            'line3': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'line3'}),
            'line4': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'line4'}),
            'rangemin': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Min'}),
            'rangemax': forms.NumberInput(attrs={'class': 'form-control',  'placeholder' : 'Max'}),
            'Invoicenumber': forms.NumberInput(attrs={'class': 'form-control',  'placeholder' : 'Max'}),
            'invoicedate': forms.DateInput(attrs={'type' :'date',  'class': 'form-control',  'placeholder' : 'Max'}),
        }