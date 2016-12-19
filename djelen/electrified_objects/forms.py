from django import forms
from django.db import models
from .models import ElectrifiedObject, ElectricityMeter, Readings

class ElectrifiedObjectForm(forms.ModelForm):
    class Meta:
        model = ElectrifiedObject
        fields = ('name', 'address')

class ElectricityMeterForm(forms.ModelForm):
    class Meta:
        model = ElectricityMeter
        fields = '__all__'

class SelectedElObjForm(forms.Form):
    selected_el_obj_id = forms.CharField()

class SelectedElMtrForm(forms.Form):
    selected_el_mtr_id = forms.CharField()

class ReadingsForms(forms.Form):
    date_readings = forms.DateField(widget=forms.DateInput(attrs={'class': 'input_date'}))
    previous_readings = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'input_tariff input'}))
    current_readings = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'input_tariff input'}))
    consumed = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'input_tariff input'}))