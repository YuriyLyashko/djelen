from django.contrib import admin
from .models import ElectrifiedObject, ElectricityMeter, Readings

# Register your models here.
admin.site.register(ElectrifiedObject)
admin.site.register(ElectricityMeter)
admin.site.register(Readings)