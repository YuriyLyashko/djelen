from django.conf.urls import url

from .views import change_el_obj, del_el_obj, add_el_obj, change_el_mtr, del_el_mtr, add_el_mtr

urlpatterns = [
    url(r'^change_el_obj/$', change_el_obj, name='change_el_obj'),
    url(r'^del_el_obj/$', del_el_obj, name='del_el_obj'),
    url(r'^add_el_obj/$', add_el_obj, name='add_el_obj'),
    url(r'^change_el_mtr/$', change_el_mtr, name='change_el_mtr'),
    url(r'^del_el_mtr/$', del_el_mtr, name='del_el_mtr'),
    url(r'^add_el_mtr/$', add_el_mtr, name='add_el_mtr'),

]