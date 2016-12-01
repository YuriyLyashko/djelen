from django import forms
from .models import ElectrifiedObject, ElectricityMeter

class ElectrifiedObjectForm(forms.ModelForm):
    class Meta:
        model = ElectrifiedObject
        fields = ('name', 'address')

class ElectricityMeterForm(forms.ModelForm):
    class Meta:
        model = ElectricityMeter
        fields = '__all__'