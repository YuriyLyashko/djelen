from django.shortcuts import render
from accounts.forms import RegisterUserForm, Login

from electrified_objects.models import ElectrifiedObject, ElectricityMeter, Readings, LastSelected
from electrified_objects.forms import ElectrifiedObjectForm, SelectedElObjForm, SelectedElMtrForm, ReadingsForms

from .forms import Texts
from tariffs.forms import TariffsForms
from tariffs.models import Tariffs

# Create your views here.
def index(request):
    print('index')
    login_form = Login()
    current_user = request.user

    texts = Texts()

    tariffs = Tariffs()

    readings = Readings()

    try:
        Tariffs.objects.get(user=current_user)
    except:
        tariffs.get_start_tariffs()
    print(tariffs.tariff_1_limit, tariffs.tariff_2_limit,tariffs.tariff_1, tariffs.tariff_2, tariffs.tariff_3)
    tariffs_forms = TariffsForms(initial={'tariff_1_limit': tariffs.tariff_1_limit,
                                          'tariff_2_limit': tariffs.tariff_2_limit,
                                          'tariff_1': tariffs.tariff_1,
                                          'tariff_2': tariffs.tariff_2,
                                          'tariff_3': tariffs.tariff_3
                                          }
                                 )
    readings_forms = ReadingsForms(initial={'date_readings': tariffs.date,
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


        return render(request, 'index.html', {'login_form': login_form,
                                              'texts': texts,
                                              'tariffs_forms': tariffs_forms,
                                              'tariffs': tariffs,
                                              'readings': readings,
                                              'readings_forms': readings_forms,

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
                                              }
                      )
    except:
        return render(request, 'index.html', {'login_form': login_form,
                                              'texts': texts,
                                              'tariffs_forms': tariffs_forms,
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
                    return render(request, 'index.html', {'login_form': login_form,
                                                          'el_objs': el_objs,
                                                          'last_selected': last_selected,
                                                          'el_mtrs': el_mtrs,
                                                          'texts': texts,
                                                          'tariffs_forms': tariffs_forms,
                                                          }
                                  )

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
                    return render(request, 'index.html', {'login_form': login_form,
                                                          'el_objs': el_objs,
                                                          'last_selected': last_selected,
                                                          'el_mtrs': el_mtrs,
                                                          'texts': texts,
                                                          'tariffs_forms': tariffs_forms,
                                                          }
                                  )