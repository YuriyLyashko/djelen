from django.db import models
from django.contrib.auth.models import User
import urllib.request
import re

# Create your models here.
class Tariffs(models.Model):
    user = models.OneToOneField(User)
    tariff_1_limit = models.PositiveIntegerField()
    tariff_2_limit = models.PositiveIntegerField()
    tariff_1 = models.DecimalField(max_digits=7, decimal_places=3)
    tariff_2 = models.DecimalField(max_digits=7, decimal_places=3)
    tariff_3 = models.DecimalField(max_digits=7, decimal_places=3)
    date = models.DateField()

    def __str__(self):
        return "Тарифи: {}, {}, {}, {}, {}".format(self.tariff_1_limit, self.tariff_2_limit,
                                           self.tariff_1,
                                           self.tariff_2,
                                           self.tariff_3
                                           )

    def update_tariffs(self):
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
            self.tariff_1 = '{0:.3f}'.format(float(tariffs_all[0]) / 100)
            self.tariff_2 = '{0:.3f}'.format(float(tariffs_all[1]) / 100)
            self.tariff_3 = '{0:.3f}'.format(float(tariffs_all[2]) / 100)

        except urllib.error.URLError:
            print('URLError')
        except ValueError:
            print('ValueError')

    def get_start_tariffs(self):
        print('get_start_tariffs')
        self.tariff_1_limit = 50
        self.tariff_2_limit = 100
        self.tariff_1 = 0.5
        self.tariff_2 = 1
        self.tariff_3 = 2
        self.date = '2016-12-17'
