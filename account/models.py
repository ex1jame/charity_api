from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    # Здесь вы можете добавить дополнительные поля, если это необходимо
    company = models.CharField(max_length=150, blank=False, null=False)


    class Meta:
        verbose_name = 'User'

