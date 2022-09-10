from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from user.utils import sex_control

phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format: '+999999999'."
    " Up to 15 digits allowed.",
)


class MyUserManager(BaseUserManager):
    def create_user(
        self,
        email,
        first_name,
        second_name,
        sex,
        phone_number,
        date_of_birth,
        password=None,
    ):
        if not email:
            raise ValueError("User must have normal email")
        if not sex_control(sex.lower()):
            sex = "Other"
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            second_name=second_name,
            sex=sex,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        first_name,
        second_name,
        sex,
        phone_number,
        date_of_birth,
        password=None,
    ):
        user = self.create_user(
            email,
            first_name=first_name,
            second_name=second_name,
            sex=sex,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    first_name = models.CharField(max_length=30, verbose_name="name")
    second_name = models.CharField(max_length=30, verbose_name="surname")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, verbose_name="phone_number", null=True
    )
    date_of_birth = models.DateField(verbose_name="birthday", null=True)
    sex = models.CharField(max_length=10, verbose_name="sex", null=True)
    creation_date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name="creation_time",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", null=True, blank=True, verbose_name="photo"
    )
    email = models.EmailField(verbose_name="Email", unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = (
        "first_name",
        "second_name",
        "phone_number",
        "date_of_birth",
        "sex",
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "MyUser"
        default_related_name = "users"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin
