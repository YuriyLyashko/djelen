from django import forms
from django.db import models
from .models import ElectrifiedObject, ElectricityMeter

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

