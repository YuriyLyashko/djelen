from django.shortcuts import render
from accounts.forms import RegisterUserForm, Login

from electrified_objects.models import ElectrifiedObject, ElectricityMeter, Readings, LastSelected
from electrified_objects.forms import ElectrifiedObjectForm, SelectedElObjForm, SelectedElMtrForm

from .forms import Texts

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


# Create your views here.
def index(request):
    print('index')
    login_form = Login()
    current_user = request.user

    texts = Texts()
    if current_user.is_anonymous:
        return render(request, 'index.html', {'login_form': login_form, 'texts': texts, })
    try:
        last_selected, el_objs, selected_el_obj, el_mtrs = get_data_for_select(current_user)
        return render(request, 'index.html', {'login_form': login_form,
                                              'el_objs': el_objs,
                                              'last_selected': last_selected,
                                              'el_mtrs': el_mtrs,
                                              'texts': texts,
                                              }
                      )
    except:
        return render(request, 'index.html', {'login_form': login_form,
                                              'texts': texts,
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
                    last_selected, el_objs, selected_el_obj, el_mtrs = get_data_for_select(current_user)
                    return render(request, 'index.html', {'login_form': login_form,
                                                          'el_objs': el_objs,
                                                          'last_selected': last_selected,
                                                          'el_mtrs': el_mtrs,
                                                          'texts': texts,
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
                                                          }
                                  )