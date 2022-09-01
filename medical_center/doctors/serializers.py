from rest_framework import serializers
from rest_framework.response import Response

from doctors.models import DoctorsCategory, Doctor
from timetable.models import TimeTable
from user.models import MyUser


class DoctorsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsCategory
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    second_name = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()
    sex = serializers.SerializerMethodField()
    date_of_birth = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    timetable = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = "__all__"

    def get_first_name(self, instance):
        return instance.user.first_name

    def get_second_name(self, instance):
        return instance.user.second_name

    def get_phone_number(self, instance):
        return instance.user.phone_number

    def get_date_of_birth(self, instance):
        return instance.user.date_of_birth

    def get_email(self, instance):
        return instance.user.email

    def get_sex(self, instance):
        return instance.user.sex

    def get_timetable(self, instance):
        try:
            timetable = TimeTable.objects.get(user=instance.user)
            print(timetable.monday)

        except Exception:
            return "doctor doesn't have timetable"
        else:
            print(timetable.monday)
            return {
                "monday": timetable.monday,
                "tuesday": timetable.tuesday,
                "wednesday": timetable.wednesday,
                "thursday": timetable.thursday,
                "friday": timetable.friday,
                "saturday": timetable.saturday,
                "sunday": timetable.sunday,
            }


class RegistrationDoctorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    second_name = serializers.CharField()
    sex = serializers.CharField()
    phone_number = serializers.CharField()
    date_of_birth = serializers.DateField()
    work_experience = serializers.CharField()
    age = serializers.IntegerField()
    education = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = Doctor
        fields = (
            "email",
            "first_name",
            "second_name",
            "sex",
            "phone_number",
            "date_of_birth",
            "work_experience",
            "age",
            "category",
            "work_experience",
            "age",
            "education",
            "password1",
            "password2",
        )

    def save(self, *args, **kwargs):
        user = MyUser.objects.create_user(
            email=self.validated_data.get("email"),
            first_name=self.validated_data.get("first_name"),
            second_name=self.validated_data.get("second_name"),
            sex=self.validated_data.get("sex", "male"),
            phone_number=self.validated_data.get("phone_number"),
            date_of_birth=self.validated_data.get("date_of_birth"),
        )
        password1 = self.validated_data.get("password1")
        password2 = self.validated_data.get("password2")
        if password1 != password2:
            raise serializers.ValidationError({password1: "Пароль не совпадает"})
        user.set_password(password1)
        user.save()
        doctor = Doctor.objects.create(
            user=user,
            category=self.validated_data.get("category"),
            work_experience=self.validated_data.get("work_experience"),
            age=self.validated_data.get("age"),
            education=self.validated_data.get("education"),
        )
        doctor.save()
        return doctor


# class UpdateDoctorSerializer(serializers.ModelSerializer):
#     first_name = serializers.SerializerMethodField()
#     second_name = serializers.SerializerMethodField()
#     phone_number = serializers.SerializerMethodField()
#     sex = serializers.SerializerMethodField()
#     date_of_birth = serializers.SerializerMethodField()
#     email = serializers.SerializerMethodField()
#     timetable = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Doctor
#         fields = '__all__'
#
#     def put_first_name(self):
