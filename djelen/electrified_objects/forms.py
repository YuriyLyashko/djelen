from django import forms
from .models import ElectrifiedObject

class ElectrifiedObjectForm(forms.ModelForm):
    class Meta:
        model = ElectrifiedObject
        fields = ('name', 'address')
