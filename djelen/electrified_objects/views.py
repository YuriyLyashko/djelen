from django.shortcuts import render, redirect
from django.contrib import messages


from electrified_objects.models import ElectrifiedObject, LastSelected, ElectricityMeter
from electrified_objects.forms import ElectrifiedObjectForm, ElectricityMeterForm

# Create your views here.
def change_el_obj(request):
    print('change_el_obj')
    current_user = request.user
    if not current_user.is_anonymous:
        if request.POST.get('but_change_el_obj'):
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

        if request.POST.get('save'):
            print(request.POST.get('save'))
            el_obj_form = ElectrifiedObjectForm(request.POST)
            if el_obj_form.is_valid():
                last_selected = LastSelected.objects.get(user_id=current_user.id)
                selected_el_obj = last_selected.el_obj
                selected_el_obj.name = el_obj_form.cleaned_data['name']
                selected_el_obj.address = el_obj_form.cleaned_data['address']
                selected_el_obj.save()
                messages.success(request, "Об'єкт відредаговано")
                return redirect('/')

        if request.POST.get('cancel'):
            print(request.POST.get('cancel'))
            return redirect('/')


    return redirect('/')

def del_el_obj(request):
    print('del_el_obj')
    current_user = request.user
    if not current_user.is_anonymous:
        if request.POST.get('but_del_el_obj'):
            el_objs = ElectrifiedObject.objects.filter(user_id=current_user.id)
            last_selected = LastSelected.objects.get(user_id=current_user.id)
            selected_el_obj_id = last_selected.el_obj_id
            el_mtrs = ElectricityMeter.objects.filter(el_object_id=selected_el_obj_id)

            el_objs_form = ElectrifiedObjectForm()
            el_mtrs_form = ElectricityMeterForm()

            return render(request, 'del_el_obj.html', {'el_objs': el_objs,
                                                          'last_selected': last_selected,
                                                          'el_mtrs': el_mtrs,
                                                          'el_objs_form': el_objs_form,
                                                          'el_mtrs_form': el_mtrs_form,
                                                          }
                          )

        if request.POST.get('del'):
            print(request.POST.get('name'))
            el_obj_form = ElectrifiedObjectForm(request.POST)
            if el_obj_form.is_valid():
                last_selected = LastSelected.objects.get(user_id=current_user.id)
                selected_el_obj = last_selected.el_obj
                if request.POST.get('name') == selected_el_obj.name:
                    selected_el_obj.delete()
                    messages.success(request, "Об'єкт видалено")
                    return redirect('/')



