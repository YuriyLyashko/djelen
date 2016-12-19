from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ElectrifiedObject(models.Model):
    name = models.CharField("Назва електрифікованого об'єкту", max_length=255)
    address = models.CharField("Адреса електрифікованого об'єкту", max_length=255, null=True, blank=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return "Назва електрифікованого об'єкту: " + str(self.name)

    @staticmethod
    def get_data_for_select(user):
        print('get_data_for_select')
        try:
            last_selected = LastSelected.objects.get(user=user)
            selected_el_obj = last_selected.el_obj
            el_mtrs = ElectricityMeter.objects.filter(el_object_id=selected_el_obj)
        except:
            last_selected = None
            selected_el_obj = None
            el_mtrs = None
        finally:
            el_objs = ElectrifiedObject.objects.filter(user=user)
            return last_selected, el_objs, selected_el_obj, el_mtrs


class ElectricityMeter(models.Model):
    number = models.CharField("Номер лічильника", max_length=255)
    el_object = models.ForeignKey(ElectrifiedObject)

    def __str__(self):
        return "Номер лічильника: {}".format(self.number)


class Readings(models.Model):
    date_readings = models.DateField(null=True)
    previous_readings = models.PositiveIntegerField(null=True)
    current_readings = models.PositiveIntegerField(null=True)
    consumed = models.PositiveIntegerField(null=True)
    electricity_meter = models.ForeignKey(ElectricityMeter)

    def __str__(self):
        return "Покази лічильника: {}, {}".format(self.previous_readings, self.current_readings)


class LastSelected(models.Model):
    user = models.OneToOneField(User)
    el_obj = models.OneToOneField(ElectrifiedObject)
    el_mtr = models.OneToOneField(ElectricityMeter, null=True)
