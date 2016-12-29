from django.db import models
from django.contrib.auth.models import User
from electrified_objects.models import ElectricityMeter

# Create your models here.
class Calculation(models.Model):
    electricity_tariff_1 = models.PositiveIntegerField()
    electricity_tariff_2 = models.PositiveIntegerField()
    electricity_tariff_3 = models.PositiveIntegerField()
    amount_electricity = models.PositiveIntegerField()
    cost_tariff_1 = models.DecimalField(max_digits=5, decimal_places=2)
    cost_tariff_2 = models.DecimalField(max_digits=5, decimal_places=2)
    cost_tariff_3 = models.DecimalField(max_digits=5, decimal_places=2)
    cost_total = models.DecimalField(max_digits=5, decimal_places=2)
    el_meter = models.ManyToManyField(ElectricityMeter)
    date = models.DateField()


    def set_costs(self, electricity_tariff_1, electricity_tariff_2, electricity_tariff_3,
                  tariff_1, tariff_2, tariff_3
                  ):
        self.cost_tariff_1 = electricity_tariff_1 * tariff_1
        self.cost_tariff_2 = electricity_tariff_2 * tariff_2
        self.cost_tariff_3 = electricity_tariff_3 * tariff_3
        self.cost_total = sum((self.cost_tariff_1, self.cost_tariff_2, self.cost_tariff_3))


    def get_calculated_data(self, tariffs, readings):
        print('get_calculated_data')
        if readings.consumed != 0:
            self.amount_electricity = readings.consumed
        else:
            self.amount_electricity = readings.current_readings - readings.previous_readings
        if 0 <= self.amount_electricity <= tariffs.tariff_1_limit:
            self.electricity_tariff_1 = self.amount_electricity
            self.electricity_tariff_2 = 0
            self.electricity_tariff_3 = 0
            self.set_costs(electricity_tariff_1=self.electricity_tariff_1,
                           electricity_tariff_2=self.electricity_tariff_2,
                           electricity_tariff_3=self.electricity_tariff_3,
                           tariff_1=tariffs.tariff_1,
                           tariff_2=tariffs.tariff_2,
                           tariff_3=tariffs.tariff_3
                           )
        elif tariffs.tariff_1_limit < self.amount_electricity <= tariffs.tariff_2_limit:
            self.electricity_tariff_1 = tariffs.tariff_1_limit
            self.electricity_tariff_2 = self.amount_electricity - self.electricity_tariff_1
            self.electricity_tariff_3 = 0
            self.set_costs(electricity_tariff_1=self.electricity_tariff_1,
                           electricity_tariff_2=self.electricity_tariff_2,
                           electricity_tariff_3=self.electricity_tariff_3,
                           tariff_1=tariffs.tariff_1,
                           tariff_2=tariffs.tariff_2,
                           tariff_3=tariffs.tariff_3
                           )
        elif tariffs.tariff_2_limit < self.amount_electricity:
            self.electricity_tariff_1 = tariffs.tariff_1_limit
            self.electricity_tariff_2 = tariffs.tariff_2_limit - tariffs.tariff_1_limit
            self.electricity_tariff_3 = self.amount_electricity - tariffs.tariff_2_limit
            self.set_costs(electricity_tariff_1=self.electricity_tariff_1,
                           electricity_tariff_2=self.electricity_tariff_2,
                           electricity_tariff_3=self.electricity_tariff_3,
                           tariff_1=tariffs.tariff_1,
                           tariff_2=tariffs.tariff_2,
                           tariff_3=tariffs.tariff_3
                           )
        else:
            raise ValueError('amount_electricity = {} < 0'.format(self.amount_electricity))

class CalculationAllData(models.Model):
    user = models.OneToOneField(User)
    tariff_1_limit = models.PositiveIntegerField()
    tariff_2_limit = models.PositiveIntegerField()
    tariff_1 = models.DecimalField(max_digits=7, decimal_places=3)
    tariff_2 = models.DecimalField(max_digits=7, decimal_places=3)
    tariff_3 = models.DecimalField(max_digits=7, decimal_places=3)
    date_tariffs = models.DateField()

    date_readings = models.DateField(null=True)
    previous_readings = models.PositiveIntegerField(null=True)
    current_readings = models.PositiveIntegerField(null=True)
    consumed = models.PositiveIntegerField(null=True)
    electricity_meter = models.ManyToManyField(ElectricityMeter)

    electricity_tariff_1 = models.PositiveIntegerField()
    electricity_tariff_2 = models.PositiveIntegerField()
    electricity_tariff_3 = models.PositiveIntegerField()
    amount_electricity = models.PositiveIntegerField()
    cost_tariff_1 = models.DecimalField(max_digits=5, decimal_places=2)
    cost_tariff_2 = models.DecimalField(max_digits=5, decimal_places=2)
    cost_tariff_3 = models.DecimalField(max_digits=5, decimal_places=2)
    cost_total = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    def __init__(self, tariffs, readings, calculation):
        self.user = tariffs.user
        self.tariff_1_limit = tariffs.tariff_1_limit
        self.tariff_2_limit = tariffs.tariff_2_limit
        self.tariff_1 = tariffs.tariff_1
        self.tariff_2 = tariffs.tariff_2
        self.tariff_3 = tariffs.tariff_3
        self.date_tariffs = tariffs.date

        self.date_readings = readings.date_readings
        self.previous_readings = readings.previous_readings
        self.current_readings = readings.current_readings
        self.consumed = readings.consumed
        self.electricity_meter = readings.electricity_meter

        self.electricity_tariff_1 = calculation.electricity_tariff_1
        self.electricity_tariff_2 = calculation.electricity_tariff_2
        self.electricity_tariff_3 = calculation.electricity_tariff_3
        self.amount_electricity = calculation.amount_electricity
        self.cost_tariff_1 = calculation.cost_tariff_1
        self.cost_tariff_2 = calculation.cost_tariff_2
        self.cost_tariff_3 = calculation.cost_tariff_3
        self.cost_total = calculation.cost_total
        self.el_meter = calculation.el_meter