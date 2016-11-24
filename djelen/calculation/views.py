from django.shortcuts import render
from accounts.forms import RegisterUserForm, Login

from electrified_objects.models import ElectrifiedObject, ElectricityMeter, Readings, LastSelected
from electrified_objects.forms import ElectrifiedObjectForm

from .forms import Texts

# Create your views here.
def index(request):
    print('index')
    login_form = Login()
    current_user = request.user

    texts = Texts()
    if current_user.is_anonymous:
        return render(request, 'index.html', {'login_form': login_form, 'texts': texts, })

    try:
        el_objs = ElectrifiedObject.objects.filter(user_id=current_user.id)
        last_selected = LastSelected.objects.get(user_id=current_user.id)
        selected_el_obj_id = last_selected.el_obj_id
        el_mtrs = ElectricityMeter.objects.filter(el_object_id=selected_el_obj_id)
        return render(request, 'index.html', {'login_form': login_form,
                                              'el_objs': el_objs,
                                              'last_selected': last_selected,
                                              'el_mtrs': el_mtrs,
                                              'texts': texts,
                                              }
                      )
    except:
        el_objs = ElectrifiedObject.objects.filter(user_id=current_user.id)

        return render(request, 'index.html', {'login_form': login_form,
                                              'el_objs': el_objs,
                                              }
                      )
    finally:
        if request.POST.get('but_select_el_obj'):
            print('but_select_el_obj')
            selected_el_obj_id = request.POST.get('select_el_obj')
            selected_el_obj = ElectrifiedObject.objects.get(pk=selected_el_obj_id)
            el_mtrs = ElectricityMeter.objects.filter(el_object_id=selected_el_obj_id)
            try:
                last_selected = LastSelected.objects.get(user_id=current_user.id)
                last_selected.el_obj = selected_el_obj
                last_selected.el_mtr = None
            except:
                last_selected = LastSelected(user=current_user, el_obj=selected_el_obj,)
            last_selected.save()
            return render(request, 'index.html', {'login_form': login_form,
                                                  'el_objs': el_objs,
                                                  'last_selected': last_selected,
                                                  'el_mtrs': el_mtrs,
                                                  }
                          )

        if request.POST.get('but_select_el_mtr'):
            print('but_select_el_mtr')
            selected_el_mtr_id = request.POST.get('select_el_mtr')
            print('selected_el_mtr_id', selected_el_mtr_id)
            last_selected_el_mtr = ElectricityMeter.objects.get(pk=selected_el_mtr_id)
            last_selected.el_mtr = last_selected_el_mtr
            print('1', last_selected.el_mtr)

            last_selected.save()
            return render(request, 'index.html', {'login_form': login_form,
                                                  'el_objs': el_objs,
                                                  'last_selected': last_selected,
                                                  'el_mtrs': el_mtrs,
                                                  }
                          )

