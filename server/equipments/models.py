from django.db import models
from django.utils.translation import gettext_lazy as _


class Weapon(models.Model):
    name = models.CharField(
        _('weapon name'),
        max_length=100,
        unique=True,
    )
    atk = models.IntegerField(
        _('weapon attack'),
        default=1,
    )
    price = models.IntegerField(
        _('weapon price'),
        default=0,
    )
    required_arm = models.IntegerField(
        _('weapon required arm'),
        default=1,
    )
    email = models.EmailField(_('email address'), blank=True)
