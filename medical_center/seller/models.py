from django.contrib.auth.base_user import BaseUserManager
from django.db import models

from timetable.models import TimeTable
from user.models import MyUser


class Seller(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, verbose_name="user")
    work_experience = models.CharField(verbose_name="work_experience", max_length=250)
    age = models.IntegerField(verbose_name="age")
    timetable = models.ForeignKey(
        TimeTable, on_delete=models.SET_NULL, null=True, verbose_name="timetable"
    )
    is_seller = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"
        db_table = "Seller"
        default_related_name = "sellers"

    def __str__(self):
        return self.user.email


class CommentSeller(models.Model):
    title = models.CharField(max_length=70, unique=True, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name="doctor")
    user = models.ForeignKey(
        MyUser, on_delete=models.SET_NULL, verbose_name="user", null=True
    )
    content = models.TextField(verbose_name="content")
    creation_date = models.DateField(
        verbose_name="creation_date", auto_now_add=True, auto_now=False
    )
    comment_on_comment = models.ForeignKey(
        "CommentSeller",
        on_delete=models.CASCADE,
        verbose_name="comment_on_comment",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "CommentSeller"
        verbose_name_plural = "CommentsDSellers"
        db_table = "CommentSeller"
        default_related_name = "comment_seller"

    def __str__(self):
        return str(self.title)
