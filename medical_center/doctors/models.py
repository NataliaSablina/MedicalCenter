from django.db import models

from timetable.models import TimeTable
from user.models import phone_regex, MyUser


class DoctorsCategory(models.Model):
    name = models.CharField(verbose_name="category_name", max_length=100, unique=True)

    class Meta:
        verbose_name = "DoctorsCategory"
        verbose_name_plural = "DoctorsCategories"
        db_table = "DoctorsCategory"
        default_related_name = "doctor_categories"

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, verbose_name="user")
    category = models.ForeignKey(
        DoctorsCategory, on_delete=models.CASCADE, verbose_name="category"
    )
    work_experience = models.CharField(verbose_name="work_experience", max_length=250)
    education = models.CharField(
        verbose_name="education", max_length=250, default="BSU"
    )
    age = models.IntegerField(verbose_name="age", default=30)
    timetable = models.ForeignKey(
        TimeTable, on_delete=models.SET_NULL, verbose_name="timetable", null=True
    )
    is_doctor = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
        db_table = "Doctors"
        default_related_name = "doctors"

    def __str__(self):
        return self.user.email


class CommentDoctor(models.Model):
    title = models.CharField(max_length=70, unique=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="doctor")
    user = models.ForeignKey(
        MyUser, on_delete=models.SET_NULL, verbose_name="user", null=True
    )
    content = models.TextField(verbose_name="content")
    creation_date = models.DateField(
        verbose_name="creation_date", auto_now_add=True, auto_now=False, null=True
    )
    comment_on_comment = models.ForeignKey(
        "CommentDoctor",
        on_delete=models.CASCADE,
        verbose_name="comment_on_comment",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "CommentDoctor"
        verbose_name_plural = "CommentsDoctors"
        db_table = "CommentDoctor"
        default_related_name = "comments_doctor"

    def __str__(self):
        return str(self.title)
