from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""

    username = models.EmailField(unique=True, null=True)

    telegram_id = models.CharField(
        max_length=200, verbose_name="Телеграм айди", null=True
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
