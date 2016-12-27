from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import *

from accounts.forms import RegisterUserForm, Login

from electrified_objects.models import ElectrifiedObject, ElectricityMeter, Readings, LastSelected
from electrified_objects.forms import ElectrifiedObjectForm, SelectedElObjForm, SelectedElMtrForm, ReadingsForms

from .forms import Texts
from tariffs.forms import TariffsForms
from tariffs.models import Tariffs

from .models import Calculation

# Create your views here.
def index(request):
    print('index')
    date_now = datetime.strftime(datetime.now(), "%Y-%m-%d")  # %H:%M:%S
    current_user = request.user
    login_form = Login()
    texts = Texts()
    readings = Readings()
    calculation = Calculation(electricity_tariff_1=0,
                              electricity_tariff_2=0,
                              electricity_tariff_3=0,
                              cost_tariff_1=0,
                              cost_tariff_2=0,
                              cost_tariff_3=0,
                              cost_total=0,
                              amount_electricity=0
                              )
    try:
        print(current_user)
        tariffs = Tariffs.objects.get(user=current_user)
        print('tariffs_db')
    except:
        tariffs = Tariffs()
        tariffs.get_start_tariffs()
    tariffs_forms = TariffsForms(initial={'tariff_1_limit': tariffs.tariff_1_limit,
                                          'tariff_2_limit': tariffs.tariff_2_limit,
                                          'tariff_1': tariffs.tariff_1,
                                          'tariff_2': tariffs.tariff_2,
                                          'tariff_3': tariffs.tariff_3
                                          }
                                 )
    readings_forms = ReadingsForms(initial={'date_readings': date_now,
                                            'previous_readings': 0,
                                            'current_readings': 0,
                                            'consumed': 0,
                                            }
                                   )


    if current_user.is_anonymous:
        if request.POST.get('update_tariffs'):
            print('update_tariffs')
            tariffs.update_tariffs()
            tariffs_forms.update_tarifs_forms(tariffs)

        if request.POST.get('calculate'):
            print('calculate')
            print(request.POST)
            readings_forms = ReadingsForms(request.POST)
            tariffs_forms = TariffsForms(request.POST)
            if readings_forms.is_valid() and tariffs_forms.is_valid():
                print('VaLiD')
                readings = Readings(date_readings=readings_forms.cleaned_data['date_readings'],
                                    previous_readings=readings_forms.cleaned_data['previous_readings'],
                                    current_readings=readings_forms.cleaned_data['current_readings'],
                                    consumed=readings_forms.cleaned_data['consumed'],
                                    )
                tariffs = Tariffs(tariff_1_limit=tariffs_forms.cleaned_data['tariff_1_limit'],
                                  tariff_2_limit=tariffs_forms.cleaned_data['tariff_2_limit'],
                                  tariff_1=tariffs_forms.cleaned_data['tariff_1'],
                                  tariff_2=tariffs_forms.cleaned_data['tariff_2'],
                                  tariff_3=tariffs_forms.cleaned_data['tariff_3'],
                                  )
                try:
                    calculation.get_calculated_data(tariffs=tariffs, readings=readings)
                except ValueError as value_error_message:
                    messages.success(request, value_error_message)
                    return redirect('/')
                readings.consumed = calculation.amount_electricity

        return render(request, 'index.html', {'login_form': login_form,
                                              'texts': texts,
                                              'tariffs_forms': tariffs_forms,
                                              'tariffs': tariffs,
                                              'readings': readings,
                                              'readings_forms': readings_forms,
                                              'calculation': calculation,
                                              }
                      )
    try:
        last_selected, el_objs, selected_el_obj, el_mtrs = ElectrifiedObject.get_data_for_select(current_user)
        return render(request, 'index.html', {'login_form': login_form,
                                              'el_objs': el_objs,
                                              'last_selected': last_selected,
                                              'el_mtrs': el_mtrs,
                                              'texts': texts,
                                              'tariffs_forms': tariffs_forms,
                                              'readings': readings,
                                              'readings_forms': readings_forms,
                                              'calculation': calculation,
                                              }
                      )
    except:
        return render(request, 'index.html', {'login_form': login_form,
                                              'texts': texts,
                                              'tariffs_forms': tariffs_forms,
                                              'readings': readings,
                                              'readings_forms': readings_forms,
                                              'calculation': calculation,
                                              }
                      )
    finally:
        if request.POST.get('selected_el_obj_id'):
            print('selected_el_obj_id')
            selected_el_obj_id = SelectedElObjForm(request.POST)
            if selected_el_obj_id.is_valid():
                print('valid obj')
                try:
                    selected_el_obj = ElectrifiedObject.objects.get(pk=selected_el_obj_id.cleaned_data['selected_el_obj_id'],
                                                                    user=current_user
                                                                    )
                except:
                    raise KeyError('ElObject not found!')
                try:
                    last_selected = LastSelected.objects.get(user=current_user)
                    last_selected.el_obj = selected_el_obj
                    last_selected.el_mtr = None
                    print('last_selected ok')
                except:
                    last_selected = LastSelected(user=current_user, el_obj=selected_el_obj,)
                finally:
                    last_selected.save()
                    last_selected, el_objs, selected_el_obj, el_mtrs = ElectrifiedObject.get_data_for_select(current_user)
                    # return render(request, 'index.html', {'login_form': login_form,
                    #                                       'el_objs': el_objs,
                    #                                       'last_selected': last_selected,
                    #                                       'el_mtrs': el_mtrs,
                    #                                       'texts': texts,
                    #                                       'tariffs_forms': tariffs_forms,
                    #                                       }
                    #               )

        if request.POST.get('selected_el_mtr_id'):
            print('selected_el_mtr_id')
            selected_el_mtr_id = SelectedElMtrForm(request.POST)
            if selected_el_mtr_id.is_valid():
                print('valid mtr')
                try:
                    last_selected = LastSelected.objects.get(user=current_user)
                    selected_el_mtr = ElectricityMeter.objects.get(pk=selected_el_mtr_id.cleaned_data['selected_el_mtr_id'],
                                                                   el_object=last_selected.el_obj
                                                                   )
                except:
                    raise KeyError('ElMtr not found!')
                finally:
                    last_selected.el_mtr = selected_el_mtr
                    last_selected.save()
                    # return render(request, 'index.html', {'login_form': login_form,
                    #                                       'el_objs': el_objs,
                    #                                       'last_selected': last_selected,
                    #                                       'el_mtrs': el_mtrs,
                    #                                       'texts': texts,
                    #                                       'tariffs_forms': tariffs_forms,
                    #                                       }
                    #               )

        if request.POST.get('update_tariffs'):
            print('update_tariffs')
            tariffs.update_tariffs()
            tariffs_forms.update_tarifs_forms(tariffs)

        if request.POST.get('save_tariffs'):
            print('save_tariffs')
            tariffs_forms = TariffsForms(request.POST)
            print(tariffs_forms)
            if tariffs_forms.is_valid():
                try:
                    tariffs = Tariffs.objects.get(user=current_user)
                    tariffs.tariff_1_limit = tariffs_forms.cleaned_data['tariff_1_limit']
                    tariffs.tariff_2_limit = tariffs_forms.cleaned_data['tariff_2_limit']
                    tariffs.tariff_1 = tariffs_forms.cleaned_data['tariff_1']
                    tariffs.tariff_2 = tariffs_forms.cleaned_data['tariff_2']
                    tariffs.tariff_3 = tariffs_forms.cleaned_data['tariff_3']
                    tariffs.date = date_now
                    tariffs.save()
                except:
                    tariffs = Tariffs(user=current_user,
                                      tariff_1_limit=tariffs_forms.cleaned_data['tariff_1_limit'],
                                      tariff_2_limit=tariffs_forms.cleaned_data['tariff_2_limit'],
                                      tariff_1=tariffs_forms.cleaned_data['tariff_1'],
                                      tariff_2=tariffs_forms.cleaned_data['tariff_2'],
                                      tariff_3=tariffs_forms.cleaned_data['tariff_3'],
                                      date=date_now
                                      )
                    tariffs.save()

        if request.POST.get('calculate'):
            print('calculate')
            print(request.POST)
            readings_forms = ReadingsForms(request.POST)
            tariffs_forms = TariffsForms(request.POST)
            if readings_forms.is_valid() and tariffs_forms.is_valid():
                print('VaLiD', current_user)
                readings = Readings(date_readings=readings_forms.cleaned_data['date_readings'],
                                    previous_readings=readings_forms.cleaned_data['previous_readings'],
                                    current_readings=readings_forms.cleaned_data['current_readings'],
                                    consumed=readings_forms.cleaned_data['consumed'],
                                    electricity_meter=last_selected.el_mtr
                                    )
                tariffs = Tariffs(user=current_user,
                                  tariff_1_limit=tariffs_forms.cleaned_data['tariff_1_limit'],
                                  tariff_2_limit=tariffs_forms.cleaned_data['tariff_2_limit'],
                                  tariff_1=tariffs_forms.cleaned_data['tariff_1'],
                                  tariff_2=tariffs_forms.cleaned_data['tariff_2'],
                                  tariff_3=tariffs_forms.cleaned_data['tariff_3'],
                                  date=readings.date_readings
                                  )
                try:
                    calculation.get_calculated_data(tariffs=tariffs, readings=readings)
                except ValueError as value_error_message:
                    messages.success(request, value_error_message)
                    return redirect('/')
                readings.consumed = calculation.amount_electricity

        return render(request, 'index.html', {'login_form': login_form,
                                              'el_objs': el_objs,
                                              'last_selected': last_selected,
                                              'el_mtrs': el_mtrs,
                                              'texts': texts,
                                              'tariffs': tariffs,
                                              'tariffs_forms': tariffs_forms,
                                              'readings': readings,
                                              'readings_forms': readings_forms,
                                              'calculation': calculation,
                                              }
                      )