from django.contrib import admin
from electrified_objects.models import ElectrifiedObject, ElectricityMeter, Readings
from tariffs.models import Tariffs

# Register your models here.
admin.site.register(ElectrifiedObject)
admin.site.register(ElectricityMeter)
admin.site.register(Readings)
admin.site.register(Tariffs)