from django import forms

from .models import ElectrifiedObject


class ElectrifiedObjectForm(forms.ModelForm):
    class Meta:
        model = ElectrifiedObject
        fields = ('name', 'address')

class ElectrifiedObjectForm(forms.Form):
    pass


class Login(forms.ModelForm):
    username = forms.CharField(label='Логін')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())