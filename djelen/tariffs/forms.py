from django import forms

class TariffsForms(forms.Form):
    tariff_1_limit = forms.IntegerField(min_value=0,
                                        initial=600,
                                        widget=forms.NumberInput(attrs={'class': 'input'})
                                        )
    tariff_1 = forms.DecimalField(min_value=0,
                                  #initial=initial_tariff_1,
                                  decimal_places=4,
                                  widget=forms.NumberInput(attrs={'class': 'input_tariff input'})
                                  )

    tariff_2_limit = forms.IntegerField(min_value=0,
                                        #initial=initial_tariff_2_limit,
                                        widget=forms.NumberInput(attrs={'class': 'input'})
                                        )
    tariff_2 = forms.DecimalField(min_value=0,
                                  #initial=initial_tariff_2,
                                  decimal_places=4,
                                  widget=forms.NumberInput(attrs={'class': 'input_tariff input'})
                                  )

    tariff_3 = forms.DecimalField(min_value=0,
                                  #initial=initial_tariff_3,
                                  decimal_places=4,
                                  widget=forms.NumberInput(attrs={'class': 'input_tariff input'})
                                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        '''
        self.fields['tariff_1_limit'].initial = 100
        self.fields['tariff_2_limit'].initial = 600
        self.fields['tariff_1'].initial = 1
        self.fields['tariff_2'].initial = 2
        self.fields['tariff_3'].initial = 3
'''