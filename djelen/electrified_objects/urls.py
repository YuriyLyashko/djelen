from django.conf.urls import url

from .views import change_el_obj

urlpatterns = [
    url(r'^$', change_el_obj, name='change_el_obj'),

]