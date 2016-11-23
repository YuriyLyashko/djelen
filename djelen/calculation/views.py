from django.shortcuts import render
from accounts.forms import RegisterUserForm, Login
from django.contrib.auth.models import User

from django import forms
from .models import ElectrifiedObject, ElectricityMeter, Readings, Tariffs, LastSelected
from .forms import ElectrifiedObjectForm

# Create your views here.
def index(request):
    print('index')
    login_form = Login()
    current_user = request.user
    if current_user.is_anonymous:
        return render(request, 'index.html', {'login_form': login_form, })
    if request.POST.get('select_el_obj'):

        id_selected_el_obj = request.POST.get('select_el_obj')
        el_mtr = ElectricityMeter.objects.filter(el_object_id=id_selected_el_obj)
        try:
            last_selected_el_obj = LastSelected.objects.get(user_id=current_user.id)
            last_selected_el_obj.el_obj_id = id_selected_el_obj
        except:
            current_user.last_selected = ElectrifiedObject.objects.get(pk=id_selected_el_obj)
            last_selected_el_obj = LastSelected(user=current_user,
                                                el_obj=ElectrifiedObject.objects.get(pk=id_selected_el_obj)
                                                )
        last_selected_el_obj.save()

        #el_mtr = ElectricityMeter.objects.filter(el_object_id=el_objs.id)

        return render(request,
                      'index.html',
                      {
                          'login_form': login_form,
                          'el_objs': el_objs,
                          'last_selected_el_obj': last_selected_el_obj,
                          'el_mtr': el_mtr,
                      }
                      )
    try:
        el_objs = ElectrifiedObject.objects.filter(user_id=current_user.id)
        last_selected_el_obj = LastSelected.objects.get(user_id=current_user.id)
        id_selected_el_obj = last_selected_el_obj.el_obj_id
        el_mtr = ElectricityMeter.objects.filter(el_object_id=id_selected_el_obj)
        return render(request,
                      'index.html',
                      {
                          'login_form': login_form,
                          'el_objs': el_objs,
                          'last_selected_el_obj': last_selected_el_obj,
                          'el_mtr': el_mtr,

                      }
                      )
    except:

        return render(request, 'index.html', {'login_form': login_form, })






