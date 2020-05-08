from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models

from server.equipments.models import Weapon


class User(AbstractUser):
    money = models.IntegerField('所持金', default=0, )
    st_point = models.IntegerField('ステータスポイント', default=0, )
    status_hp = models.IntegerField('最大体力', default=10, )
    status_arm = models.IntegerField('腕力', default=1, )
    status_luck = models.IntegerField('幸運', default=1, )
    hp = models.IntegerField('体力', default=1, )
    weapon = models.ForeignKey(Weapon, on_delete=models.SET_NULL, blank=True, null=True, related_name='users',
                               verbose_name='武器', )
