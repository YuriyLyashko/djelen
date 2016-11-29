from django.conf.urls import url

from .views import change_el_obj, del_el_obj

urlpatterns = [
    url(r'^change_el_obj/$', change_el_obj, name='change_el_obj'),
    url(r'^del_el_obj/$', del_el_obj, name='del_el_obj'),

]