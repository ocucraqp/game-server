from django.db import models

from server.accounts.models import User


class EnemyType(models.Model):
    name = models.CharField('名前', max_length=100, )
    status_hp = models.IntegerField('最大体力', blank=False, null=False, default=1, )
    atk = models.IntegerField('攻撃力', blank=False, null=False, default=1, )
    reward_money = models.IntegerField('報酬金', blank=False, null=False, default=1, )
    reward_st_point = models.IntegerField('報酬ステータスポイント', blank=False, null=False, default=1, )
    image = models.ImageField('画像', upload_to='battles/enemytypes/images/')
    enabled = models.BooleanField('有効', default=True,
                                  help_text=('Designates whether this enemy should be treated as active. '
                                             'Unselect this instead of deleting enemy data.'), )

    class Meta:
        verbose_name = '敵の種類'
        verbose_name_plural = '敵の種類'

    def __str__(self):
        return self.name


class Enemy(models.Model):
    type = models.ForeignKey('EnemyType', on_delete=models.CASCADE, related_name='enemies',
                             verbose_name='敵の種類')
    hp = models.IntegerField('体力', blank=False, null=False, )

    class Meta:
        verbose_name = '敵'
        verbose_name_plural = '敵'


class Contribution(models.Model):
    enemy = models.ForeignKey('Enemy', on_delete=models.CASCADE, related_name='contributions',
                              verbose_name='敵')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='contributions',
                             verbose_name='ユーザー')
    damage = models.IntegerField('貢献ダメージ', blank=False, null=False, default=0, )
    received = models.BooleanField('受け取り済み', default=False, help_text=('Designates whether the user got rewards. '), )

    class Meta:
        verbose_name = '貢献度'
        verbose_name_plural = '貢献度'
