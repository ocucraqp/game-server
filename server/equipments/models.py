from django.db import models
from django.utils.translation import gettext_lazy as _


class Weapon(models.Model):
    name = models.CharField(
        _('名前'),
        max_length=100,
        unique=True,
    )
    atk = models.IntegerField(
        _('攻撃力'),
        default=1,
    )
    price = models.IntegerField(
        _('値段'),
        default=0,
    )
    required_arm = models.IntegerField(
        _('必要腕力'),
        default=1,
    )

    class Meta:
        verbose_name = '武器'
        verbose_name_plural = '武器'
