from django.db import models
from user.models import phone_regex, MyUser


class DoctorsCategory(models.Model):
    name = models.CharField(verbose_name="category_name", max_length=100, unique=True)

    class Meta:
        verbose_name = "DoctorsCategory"
        verbose_name_plural = "DoctorsCategories"
        db_table = "DoctorsCategory"

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
    is_doctor = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
        db_table = "Doctors"

    def __str__(self):
        return self.user.email


class CommentDoctor(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="doctor")
    user = models.ForeignKey(
        MyUser, on_delete=models.SET_NULL, verbose_name="user", null=True
    )
    content = models.TextField(verbose_name="content")
    creation_date = models.DateField(
        verbose_name="creation_date", auto_now_add=True, auto_now=False
    )

    class Meta:
        verbose_name = "CommentDoctor"
        verbose_name_plural = "CommentsDoctors"
        db_table = "CommentDoctor"

    def __str__(self):
        return self.pk, self.content[:20]
