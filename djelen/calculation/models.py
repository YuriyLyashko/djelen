from django.db import models
from django.contrib.auth.models import User
from electrified_objects.models import ElectricityMeter

# Create your models here.
class Calculation(models.Model):
    amount_electricity = models.PositiveIntegerField()
    electricity_tariff_1 = models.PositiveIntegerField()
    electricity_tariff_2 = models.PositiveIntegerField()
    electricity_tariff_3 = models.PositiveIntegerField()
    cost_tariff_1 = models.DecimalField(max_digits=5, decimal_places=2)
    cost_tariff_2 = models.DecimalField(max_digits=5, decimal_places=2)
    cost_tariff_3 = models.DecimalField(max_digits=5, decimal_places=2)
    cost_total = models.DecimalField(max_digits=5, decimal_places=2)
    el_meter = models.ManyToManyField(ElectricityMeter)

    def get_calculated_data(self, readings):
        print('get_calculated_data')
        self.amount_electricity = readings.current_readings - readings.previous_readings
        #if 0 <= self.amount_electricity <= temp_readings.
