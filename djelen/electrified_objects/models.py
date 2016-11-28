from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ElectrifiedObject(models.Model):
    name = models.CharField("Назва електрифікованого об'єкту", max_length=255)
    address = models.CharField("Адреса електрифікованого об'єкту", max_length=255, null=True, blank=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return "Назва електрифікованого об'єкту: " + str(self.name)


class ElectricityMeter(models.Model):
    number = models.CharField("Номер лічильника", max_length=255)
    el_object = models.ForeignKey(ElectrifiedObject)

    def __str__(self):
        return "Номер лічильника: {}".format(self.number)


class Readings(models.Model):
    previous_readings = models.PositiveIntegerField("Попередні покази лічильника")
    current_readings = models.PositiveIntegerField("Поточні покази лічильника")
    electricity_meter = models.ForeignKey(ElectricityMeter)

    def __str__(self):
        return "Покази лічильника: {}, {}".format(self.previous_readings, self.current_readings)


class LastSelected(models.Model):
    user = models.OneToOneField(User)
    el_obj = models.OneToOneField(ElectrifiedObject)
    el_mtr = models.OneToOneField(ElectricityMeter, null=True)
