from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from user.models import MyUser


class Seller(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, verbose_name='user')
    work_experience = models.CharField(verbose_name='work_experience', max_length=250)
    age = models.IntegerField(verbose_name='age')
    is_seller = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = 'Sellers'
        db_table = "Seller"

    def __str__(self):
        return self.user.email

