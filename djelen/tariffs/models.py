from django.db import models
from django.contrib.auth.models import User
import urllib.request
import re

# Create your models here.
class Tariffs(models.Model):
    user = models.OneToOneField(User)
    tariff_1_limit = models.PositiveIntegerField()
    tariff_2_limit = models.PositiveIntegerField()
    tariff_1 = models.FloatField()
    tariff_2 = models.FloatField()
    tariff_3 = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return "Тарифи: {}, {}, {}".format(self.tarrif_limit_1, self.tarrif_limit_2, self.tarrif_limit_3)

    def get_tariffs_inet(self):
        '''
        Отримання тарифів з сайту Київенерго
        '''
        print('tariffs_inet')
        try:
            u_o = urllib.request.urlopen('http://kyivenergo.ua/odnozonni_lichilniki/')
            u_o = u_o.read().decode(encoding="utf-8", errors="ignore")
            #        print(u_o)
            tariffs_all = [tar.replace(',', '.') for tar in re.findall
            (r'<td>(\w+.\w+)\W+\w+\W+</tr>', u_o)]
            #        print(tarifi_all)
            self.tariff_1_limit = (re.findall(r'спожитий до (\w+)', u_o)[0])
            self.tariff_2_limit = (re.findall(r'спожитий понад (\w+)', u_o)[1])
            self.tariff_1 = (float(tariffs_all[0]) / 100)
            self.tariff_2 = (float(tariffs_all[1]) / 100)
            self.tariff_3 = (float(tariffs_all[2]) / 100)
            #message_answer.set('{}'.format(message_tariffs_received_from_inet))

        except urllib.error.URLError:
            print('URLError')
            #show_error()
        except ValueError:
            print('ValueError')
            #show_error()

    #@staticmethod
    def get_start_tariffs(self):
        self.tariff_1_limit = 100
        self.tariff_2_limit = 500
        self.tariff_1 = 0.5
        self.tariff_2 = 1
        self.tariff_3 = 2
        self.date = 2016-12-17
        #return tariff_1_limit, tariff_2_limit, tariff_1, tariff_2, tariff_3, date
