from django.conf.urls import url

from .views import registration, log_in, log_out

urlpatterns = [
    url(r'^$', registration, name='registration'),
    url(r'^log_in/', log_in, name='log_in'),
    url(r'^log_out/', log_out, name='log_out'),

]