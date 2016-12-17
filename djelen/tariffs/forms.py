from django import forms

class TariffsForms(forms.Form):
    tariff_1_limit = forms.IntegerField(min_value=0, initial=100, widget=forms.NumberInput(attrs={'class': 'input'}))
    tariff_1 = forms.DecimalField(min_value=0, initial=0.5, decimal_places=4, widget=forms.NumberInput(attrs={'class': 'input_tariff input'}))

    tariff_2_limit = forms.IntegerField(min_value=0, initial=600, widget=forms.NumberInput(attrs={'class': 'input'}))
    tariff_2 = forms.DecimalField(min_value=0, initial=1, decimal_places=4, widget=forms.NumberInput(attrs={'class': 'input_tariff input'}))

    tariff_3 = forms.DecimalField(min_value=0, initial=2, decimal_places=4, widget=forms.NumberInput(attrs={'class': 'input_tariff input'}))