# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal
from .utilities import get_timestamp_path
from django.db.models.signals import post_save


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Слать оповещения о новых комментариях')


    class Meta(AbstractUser.Meta):
        pass


user_registrated = Signal(providing_args=['instance'])


def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registrated.connect(user_registrated_dispatcher)




# Create your models here.
