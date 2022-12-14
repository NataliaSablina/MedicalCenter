from django.core.validators import RegexValidator
from django.db import models

# timetable_regex = RegexValidator(
#     regex=r"/^(0[1-9][ap]\.m|1[0-2][p]a\.m)[-](0[1-9][ap]\.m|1[0-2][ap]\.m)/gm",
#     message="Work hours must be entered in the format: '99a.m(p.m)-99a.m(p.m)'."
#     " Without spaces",
# )


class TimeTable(models.Model):
    name = models.CharField(verbose_name="name", max_length=250)
    monday = models.CharField(
        # validators=[timetable_regex],
        max_length=20,
        verbose_name="monday",
        blank=True,
        null=True,
    )
    tuesday = models.CharField(
        # validators=[timetable_regex],
        max_length=20,
        verbose_name="tuesday",
        blank=True,
        null=True,
    )
    wednesday = models.CharField(
        # validators=[timetable_regex],
        max_length=20,
        verbose_name="wednesday",
        blank=True,
        null=True,
    )
    thursday = models.CharField(
        # validators=[timetable_regex],
        max_length=20,
        verbose_name="thursday",
        blank=True,
        null=True,
    )
    friday = models.CharField(
        # validators=[timetable_regex],
        max_length=20,
        verbose_name="friday",
        blank=True,
        null=True,
    )
    saturday = models.CharField(
        # validators=[timetable_regex],
        max_length=20,
        verbose_name="saturday",
        blank=True,
        null=True,
    )
    sunday = models.CharField(
        # validators=[timetable_regex],
        max_length=20,
        verbose_name="sunday",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "DoctorTimeTable"
        verbose_name_plural = "DoctorTimeTables"
        db_table = "DoctorTimeTable"

    def __str__(self):
        return self.name
