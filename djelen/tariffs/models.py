from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tariffs(models.Model):
    tarrif_limit_1 = models.FloatField()
    tarrif_limit_2 = models.FloatField()
    tarrif_limit_3 = models.FloatField()
    user = models.OneToOneField(User)

    def __str__(self):
        return "Тарифи: {}, {}, {}".format(self.tarrif_limit_1, self.tarrif_limit_2, self.tarrif_limit_3)