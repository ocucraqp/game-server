from django.db import models
from ..accounts.models import User
from django.core.validators import MinValueValidator

class EnemyType(models.Model):
    name = models.CharField(
        '名前',
        max_length=100,
        unique=True,
        help_text='Required. 100 characters or fewer. Letters, digits and @/./+/-/_ only.',
        # validators=
        error_messages={
            'unique': "An enemy with that name already exists."
        },
    )
    status_hp = models.IntegerField(
        '最大体力',
        blank=False,
        null=False,
        default=1,
        validators=[MinValueValidator(1, 'HP must 1 or more.')],
    )
    atk = models.IntegerField(
        '攻撃力',
        blank=False,
        null=False,
        default=1,
        validators=[MinValueValidator(1, 'Attack point must 1 or more.')],
    )
    reward_money = models.IntegerField(
        '報酬金',
        blank=False,
        null=False,
        default=1,
        validators=[MinValueValidator(1, 'Reward money must 1 or more.')],
    )
    reward_st_point = models.IntegerField(
        '報酬ステータスポイント',
        blank=False,
        null=False,
        default=1,
        validators=[MinValueValidator(1, 'Reward status point must 1 or more.')],
    )
    image = models.ImageField(
        '画像',
        upload_to='images/'
    )
    enabled = models.BooleanField(
        '有効',
        default=True,
        help_text=(
            'Designates whether this enemy should be treated as active. '
            'Unselect this instead of deleting enemy data.'
        ),
    )
    class Meta:
        verbose_name = '敵'
        verbose_name_plural = '敵'
    def __str__(self):
        return self.name

class Enemy(models.Model):
    type = models.ForeignKey(
        EnemyType,
        on_delete=models.CASCADE
    )
    hp = models.IntegerField(
        '体力',
        blank=False,
        null=False,
        default=type.status_hp,
    )

class Contribution(models.Model):
    enemy = models.ForeignKey(
        Enemy,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    damage = models.IntegerField(
        '貢献ダメージ',
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(1, 'Contributed damage must 0 or more.')],
    )
    received = models.BooleanField(
        '受け取り済み',
        default=False,
        help_text=(
            'Designates whether the user got rewards. '
        ),
    )