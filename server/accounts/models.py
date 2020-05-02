from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from server.equipments.models import Weapon


class User(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    money = models.IntegerField(
        _('所持金'),
        default=0,
    )
    st_point = models.IntegerField(
        _('ステータスポイント'),
        default=0,
    )
    status_hp = models.IntegerField(
        _('最大体力'),
        default=1,
    )
    status_arm = models.IntegerField(
        _('腕力'),
        default=1,
    )
    status_luck = models.IntegerField(
        _('幸運'),
        default=1,
    )
    hp = models.IntegerField(
        _('体力'),
        default=1,
    )
    weapon = models.ForeignKey(Weapon, on_delete=models.SET_NULL, blank=True, null=True, related_name='users',
                               verbose_name='武器')

    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'
