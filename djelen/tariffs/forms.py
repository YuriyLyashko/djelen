from django import forms

class TariffsForms(forms.Form):
    tariff_1_limit = forms.IntegerField(min_value=0,
                                        widget=forms.NumberInput(attrs={'class': 'input'})
                                        )
    tariff_1 = forms.DecimalField(min_value=0,
                                  decimal_places=4,
                                  widget=forms.NumberInput(attrs={'class': 'input_tariff input'})
                                  )

    tariff_2_limit = forms.IntegerField(min_value=0,
                                        widget=forms.NumberInput(attrs={'class': 'input'})
                                        )
    tariff_2 = forms.DecimalField(min_value=0,
                                  decimal_places=4,
                                  widget=forms.NumberInput(attrs={'class': 'input_tariff input'})
                                  )

    tariff_3 = forms.DecimalField(min_value=0,
                                  decimal_places=4,
                                  widget=forms.NumberInput(attrs={'class': 'input_tariff input'})
                                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update_tarifs_forms(self, tariffs):
        self.initial['tariff_1_limit'] = tariffs.tariff_1_limit
        self.initial['tariff_2_limit'] = tariffs.tariff_2_limit
        self.initial['tariff_1'] = tariffs.tariff_1
        self.initial['tariff_2'] = tariffs.tariff_2
        self.initial['tariff_3'] = tariffs.tariff_3