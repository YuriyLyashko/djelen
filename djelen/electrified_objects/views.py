from django.shortcuts import render, redirect, reverse
from django.contrib import messages


from electrified_objects.models import ElectrifiedObject, LastSelected, ElectricityMeter
from electrified_objects.forms import ElectrifiedObjectForm, ElectricityMeterForm

# Create your views here.
def change_el_obj(request):
    print('change_el_obj')
    current_user = request.user
    if not current_user.is_anonymous:
        if request.POST.get('but_change_el_obj'):
            last_selected, el_objs, selected_el_obj, el_mtrs = ElectrifiedObject.get_data_for_select(current_user)
            if selected_el_obj:
                return render(request, 'change_el_obj.html', {'el_objs': el_objs,
                                                              'last_selected': last_selected,
                                                              'el_mtrs': el_mtrs,
                                                              }
                              )
            else:
                messages.success(request, "Оберіть електрифікований об'єкт для редагування")
                return redirect('/')

        if request.POST.get('save'):
            print(request.POST.get('save'))
            el_obj_form = ElectrifiedObjectForm(request.POST)
            if el_obj_form.is_valid():
                try:
                    ElectrifiedObject.objects.get(name=el_obj_form.cleaned_data['name'])
                    messages.success(request, "Електрифікований об'єкт з такою назвою вже існує")
                except:
                    last_selected = LastSelected.objects.get(user=current_user)
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
            last_selected, el_objs, selected_el_obj, el_mtrs = ElectrifiedObject.get_data_for_select(current_user)
            if selected_el_obj:
                print(selected_el_obj)
                return render(request, 'del_el_obj.html', {'el_objs': el_objs,
                                                              'last_selected': last_selected,
                                                              'el_mtrs': el_mtrs,
                                                              }
                              )
            else:
                messages.success(request, "Оберіть електрифікований об'єкт для видалення")
                return redirect('/')

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
                else:
                    messages.success(request, "Назву об'єкту введено не вірно!")
                    return redirect('/')
            else:
                messages.success(request, "Назву об'єкту не введено!")
                return redirect('/')

        if request.POST.get('cancel'):
            print(request.POST.get('cancel'))
            return redirect('/')


def add_el_obj(request):
    print('add_el_obj')
    current_user = request.user
    if not current_user.is_anonymous:
        if request.POST.get('but_add_el_obj'):
            print('but_add_el_obj')
            try:
                last_selected, el_objs, selected_el_obj, el_mtrs = ElectrifiedObject.get_data_for_select(current_user)
                el_objs_form = ElectrifiedObjectForm()
                return render(request, 'add_el_obj.html', {'el_objs': el_objs,
                                                           'last_selected': last_selected,
                                                           'el_mtrs': el_mtrs,
                                                           'el_objs_form': el_objs_form,
                                                           }
                              )
            except:
                el_objs_form = ElectrifiedObjectForm()
                return render(request, 'add_el_obj.html', {'el_objs_form': el_objs_form,})

        if request.POST.get('add'):
            print('add')
            el_obj_form = ElectrifiedObjectForm(request.POST)
            if el_obj_form.is_valid():
                print('is_valid')
                if not ElectrifiedObject.objects.filter(user=current_user, name=el_obj_form.cleaned_data['name']).exists():
                    print('yes')
                    new_el_obj = ElectrifiedObject(name=el_obj_form.cleaned_data['name'],
                                                   address=el_obj_form.cleaned_data['address'],
                                                   user=current_user
                                                   )
                    new_el_obj.save()
                    messages.success(request, "Новий електрифікований об'єкт створено")
                    return redirect('/')
                else:
                    messages.success(request, "Електрифікований об'єкт з такою назвою вже існує")
                    return redirect('/')

        if request.POST.get('cancel'):
            print(request.POST.get('cancel'))
            return redirect('/')


def change_el_mtr(request):
    print('change_el_mtr')
    current_user = request.user
    if not current_user.is_anonymous:
        if request.POST.get('but_change_el_mtr'):
            last_selected, el_objs, selected_el_obj, el_mtrs = ElectrifiedObject.get_data_for_select(current_user)
            if last_selected.el_mtr:
                el_mtr_form = ElectricityMeterForm()
                return render(request, 'change_el_mtr.html', {'el_objs': el_objs,
                                                              'last_selected': last_selected,
                                                              'el_mtrs': el_mtrs,
                                                              'el_mtr_form': el_mtr_form,
                                                              }
                              )
            else:
                messages.success(request, "Оберіть лічильник для редагування")
                return redirect('/')

        if request.POST.get('save'):
            print('save')
            el_mtr_form = ElectricityMeterForm(request.POST)
            print(el_mtr_form)
            if el_mtr_form.is_valid():
                last_selected = LastSelected.objects.get(user=current_user)
                selected_el_mtr = last_selected.el_mtr
                selected_el_mtr.number = el_mtr_form.cleaned_data['number']
                if selected_el_mtr.el_object != el_mtr_form.cleaned_data['el_object']:
                    last_selected.el_mtr = None
                    last_selected.save()
                selected_el_mtr.el_object = el_mtr_form.cleaned_data['el_object']
                selected_el_mtr.save()
                messages.success(request, "Лічильник відредаговано")
                return redirect('/')
            else:
                messages.success(request, "Введено не коректні дані")
                return reverse('change_el_mtr')

        if request.POST.get('cancel'):
            print(request.POST.get('cancel'))
            return redirect('/')


def del_el_mtr(request):
    print('del_el_mtr')
    current_user = request.user
    if not current_user.is_anonymous:
        if request.POST.get('but_del_el_mtr'):
            last_selected, el_objs, selected_el_obj, el_mtrs = ElectrifiedObject.get_data_for_select(current_user)
            if last_selected.el_mtr:
                el_mtr_form = ElectricityMeterForm()
                return render(request, 'del_el_mtr.html', {'el_objs': el_objs,
                                                           'last_selected': last_selected,
                                                           'el_mtrs': el_mtrs,
                                                           'el_mtr_form': el_mtr_form,
                                                           }
                              )
            else:
                messages.success(request, "Оберіть лічильник для видалення")
                return redirect('/')

        if request.POST.get('del'):
            print(request.POST.get('number'))
            el_mtr_form = ElectricityMeterForm(request.POST)
            if el_mtr_form.is_valid():
                last_selected = LastSelected.objects.get(user_id=current_user.id)
                selected_el_mtr = last_selected.el_mtr
                if request.POST.get('number') == selected_el_mtr.number and \
                                int(request.POST.get('el_object')) == selected_el_mtr.el_object.id:
                    selected_el_mtr.delete()
                    messages.success(request, "Лічильник видалено")
                    return redirect('/')
                else:
                    messages.success(request, "Дані підтвердження введено не вірно!")
                    return redirect('/')
            else:
                messages.success(request, "Назву лічильника не введено!")
                return redirect('/')

        if request.POST.get('cancel'):
            print(request.POST.get('cancel'))
            return redirect('/')


def add_el_mtr(request):
    print('add_el_mtr')
    current_user = request.user
    if not current_user.is_anonymous:
        if request.POST.get('but_add_el_mtr'):
            print('but_add_el_mtr')
            try:
                last_selected, el_objs, selected_el_obj, el_mtrs = ElectrifiedObject.get_data_for_select(current_user)
                if not selected_el_obj:
                    raise IndexError
                el_mtr_form = ElectricityMeterForm()
                return render(request, 'add_el_mtr.html', {'el_objs': el_objs,
                                                           'last_selected': last_selected,
                                                           'el_mtrs': el_mtrs,
                                                           'el_mtr_form': el_mtr_form,
                                                           }
                              )
            except:
                messages.success(request, "Оберіть електрифікований об'єкт")
                return redirect('/')

        if request.POST.get('add'):
            print('add')
            el_mtr_form = ElectricityMeterForm(request.POST)
            if el_mtr_form.is_valid():
                print('valid')
                print(ElectricityMeter.objects.filter(el_object=el_mtr_form.cleaned_data['el_object']))
                if not ElectricityMeter.objects.filter(el_object=el_mtr_form.cleaned_data['el_object'],
                                                       number=el_mtr_form.cleaned_data['number']
                                                       ).exists():
                    new_el_mtr = ElectricityMeter(number=el_mtr_form.cleaned_data['number'],
                                                   el_object=el_mtr_form.cleaned_data['el_object'],
                                                   )
                    new_el_mtr.save()
                    messages.success(request, "Новий лічильник створено")
                    return redirect('/')
                else:
                    messages.success(request, "Лічильник з таким номером вже існує")
                    return redirect('/')

        if request.POST.get('cancel'):
            print(request.POST.get('cancel'))
            return redirect('/')