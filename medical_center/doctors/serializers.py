from rest_framework import serializers
from rest_framework.response import Response

from doctors.models import DoctorsCategory, Doctor, CommentDoctor
from timetable.models import TimeTable
from timetable.serializers import TimeTableSerializer
from user.models import MyUser


class DoctorsCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = DoctorsCategory
        fields = "__all__"

    # def create(self, validated_data):
    #     return DoctorsCategory.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", self.create(validated_data))
    #     instance.save()
    #     return instance


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
        timetable = instance.timetable
        if timetable is None:
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
            "timetable",
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
            raise serializers.ValidationError({password1: "password1 != password2"})
        user.set_password(password1)
        user.save()
        doctor = Doctor.objects.create(
            user=user,
            category=self.validated_data.get("category"),
            work_experience=self.validated_data.get("work_experience"),
            age=self.validated_data.get("age"),
            education=self.validated_data.get("education"),
            timetable=self.validated_data.get("timetable"),
        )
        doctor.save()
        return doctor


class CommentDoctorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CommentDoctor
        fields = "__all__"
        lookup_field = "title"


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    second_name = serializers.CharField()
    sex = serializers.CharField()
    phone_number = serializers.CharField()
    date_of_birth = serializers.DateField()

    class Meta:
        model = MyUser
        exclude = [
            "password",
            "last_login",
            "creation_date",
            "is_active",
            "is_admin",
        ]

    def update(self, instance, validated_data):
        user = instance
        user_data = validated_data
        user.first_name = user_data.get("first_name", user.first_name)
        user.second_name = user_data.get("second_name", user.second_name)
        user.email = user_data.get("email", user.email)
        user.sex = user_data.get("sex", user.sex)
        user.phone_number = user_data.get("phone_number", user.phone_number)
        user.date_of_birth = user_data.get("date_of_birth", user.date_of_birth)
        user.photo = user_data.get("photo", user.photo)
        user.save()
        return user


class DoctorUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    work_experience = serializers.CharField()
    age = serializers.IntegerField()
    education = serializers.CharField()

    class Meta:
        model = Doctor
        fields = (
            "id",
            "user",
            "work_experience",
            "age",
            "education",
            "category",
            "timetable",
        )

    def update(self, instance, validated_data):
        user = MyUser.objects.get(email=instance.user.email)
        user_data = validated_data.get("user")
        user_serializer = UserSerializer(user, data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        instance.age = validated_data.get("age", instance.age)
        instance.education = validated_data.get("education", instance.education)
        instance.work_experience = validated_data.get(
            "work_experience", instance.work_experience
        )
        category_data = validated_data.get("category")
        category = DoctorsCategory.objects.get(name=category_data)
        instance.category = category
        timetable_data = validated_data.get("timetable")
        timetable = TimeTable.objects.get(name=timetable_data)
        instance.timetable = timetable
        instance.save()

        return instance
