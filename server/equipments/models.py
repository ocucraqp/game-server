from django.db import models


class Weapon(models.Model):
    name = models.CharField(
        '名前',
        max_length=100,
        unique=True,
    )
    atk = models.IntegerField(
        '攻撃力',
        default=1,
    )
    price = models.IntegerField(
        '値段',
        default=0,
    )
    required_arm = models.IntegerField(
        '必要腕力',
        default=1,
    )

    class Meta:
        verbose_name = '武器'
        verbose_name_plural = '武器'
