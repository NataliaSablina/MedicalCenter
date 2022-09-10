from rest_framework import serializers
from rest_framework.response import Response

from doctors.models import DoctorsCategory, Doctor, CommentDoctor
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


class CommentDoctorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CommentDoctor
        fields = "__all__"
        lookup_field = "title"


class DoctorUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    second_name = serializers.CharField()
    sex = serializers.CharField()
    phone_number = serializers.CharField()
    date_of_birth = serializers.DateField()
    work_experience = serializers.CharField()
    age = serializers.IntegerField()
    education = serializers.CharField()

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
            "age",
            "education",
        )

        def save(self, *args, **kwargs):
            print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
            doctor = Doctor.objects.get(
                user__email=self.validated_data.get("email"),
            )
            doctor.user.first_name = self.validated_data.get(
                "first_name", doctor.user.first_name
            )
            doctor.user.second_name = self.validated_data.get(
                "second_name", doctor.user.second_name
            )
            doctor.user.email = self.validated_data.get("email", doctor.user.email)
            doctor.user.sex = self.validated_data.get("sex", doctor.user.sex)
            doctor.user.phone_number = self.validated_data.get(
                "phone_number", doctor.user.phone_number
            )
            doctor.user.date_of_birth = self.validated_data.get(
                "date_of_birth", doctor.user.date_of_birth
            )
            doctor.age = self.validated_data.get("age", doctor.age)
            doctor.education = self.validated_data.get("education", doctor.education)
            doctor.work_experience = self.validated_data.get(
                "work_experience", doctor.work_experience
            )
            doctor.category = self.validated_data.get("category", doctor.category)

            instance = super().save()
            return instance
            doctor.save()
            return doctor

        def create(self, validated_data):
            print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
            print(validated_data)

        def update(self, instance, validated_data):
            print(
                "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
            )
            instance.user.first_name = validated_data.get(
                "first_name", instance.user.first_name
            )
            instance.user.second_name = validated_data.get(
                "second_name", instance.user.second_name
            )
            instance.user.email = validated_data.get("email", instance.user.email)
            instance.user.sex = validated_data.get("sex", instance.user.sex)
            instance.user.phone_number = validated_data.get(
                "phone_number", instance.user.phone_number
            )
            instance.user.date_of_birth = validated_data.get(
                "date_of_birth", instance.user.date_of_birth
            )
            instance.age = validated_data.get("age", instance.age)
            instance.education = validated_data.get("education", instance.education)
            instance.work_experience = validated_data.get(
                "work_experience", instance.work_experience
            )
            instance.category = validated_data.get("category", instance.category)

            instance = super().update(instance, validated_data)
            return instance
