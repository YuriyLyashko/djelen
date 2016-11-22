from django.shortcuts import render
from accounts.forms import RegisterUserForm, Login
from .models import ElectrifiedObject, ElectricityMeter, Readings, Tariffs

# Create your views here.
def index(request):
    print('index')
    login_form = Login()
    #el_obj = ElectrifiedObject.objects.get(pk=1)
    #el_meters = ElectricityMeter.objects.filter(el_object=el_obj)
    #readings = Readings.objects.filter()
    #tariffs = Tariffs.objects.all()
    return render(request,
                  'index.html',
                  {
                      'login_form': login_form,
                        #'el_obj': el_obj, 'el_meters': el_meters, 'readings': readings, 'tariffs': tariffs
                  }
                  )