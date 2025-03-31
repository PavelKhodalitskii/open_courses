from django.db import models

from django.contrib.auth.models import AbstractUser

class ExtendedUser(AbstractUser):
    '''
    Расширенная модель User из django.contrib.auth
    '''
    email = models.EmailField("Электронная почта", blank=True, null=True)
    patronymic = models.CharField(max_length=255, null=True, blank=True, verbose_name="Отчество")