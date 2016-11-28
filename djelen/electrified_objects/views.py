from django.shortcuts import render

from electrified_objects.models import ElectrifiedObject, LastSelected, ElectricityMeter
from electrified_objects.forms import ElectrifiedObjectForm, ElectricityMeterForm

# Create your views here.
def change_el_obj(request):
    print('change_el_obj')
    current_user = request.user
    if not current_user.is_anonymous:
        print(current_user)
        if request.POST.get('but_change_el_obj'):
            print(request.POST.get('but_change_el_obj'))
            el_objs = ElectrifiedObject.objects.filter(user_id=current_user.id)
            last_selected = LastSelected.objects.get(user_id=current_user.id)
            selected_el_obj_id = last_selected.el_obj_id
            el_mtrs = ElectricityMeter.objects.filter(el_object_id=selected_el_obj_id)

            el_objs_form = ElectrifiedObjectForm()
            el_mtrs_form = ElectricityMeterForm()

            return render(request, 'change_el_obj.html', {'el_objs': el_objs,
                                                          'last_selected': last_selected,
                                                          'el_mtrs': el_mtrs,
                                                          'el_objs_form': el_objs_form,
                                                          'el_mtrs_form': el_mtrs_form,

                                                          }
                          )