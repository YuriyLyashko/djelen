from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ElectrifiedObject(models.Model):
    name = models.CharField("Назва електрифікованого об'єкту", max_length=255)
    address = models.CharField("Адреса електрифікованого об'єкту", max_length=255, null=True)

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

class Tariffs(models.Model):
    tarrif_limit_1 = models.FloatField()
    tarrif_limit_2 = models.FloatField()
    tarrif_limit_3 = models.FloatField()
    user = models.OneToOneField(User)

    def __str__(self):
        return "Тарифи: {}, {}, {}".format(self.tarrif_limit_1, self.tarrif_limit_2, self.tarrif_limit_3)