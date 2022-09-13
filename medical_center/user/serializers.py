from rest_framework import serializers
from doctors.models import Doctor
from user.models import MyUser


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = MyUser
        fields = [
            "email",
            "first_name",
            "second_name",
            "sex",
            "phone_number",
            "date_of_birth",
            "password1",
            "password2",
        ]

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
        return user


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    creation_date = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = "__all__"


class RegistrationSuperUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = MyUser
        fields = [
            "email",
            "first_name",
            "second_name",
            "sex",
            "phone_number",
            "date_of_birth",
            "password1",
            "password2",
        ]

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
        user.is_admin = True
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
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


class SuperUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        exclude = [
            "password",
            "last_login",
            "creation_date",
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
        user.is_active = user_data.get("is_active", user.is_active)
        user.is_admin = user_data.get("is_admin", user.is_admin)
        user.save()
        return user


# class DoctorUpdateSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     work_experience = serializers.CharField()
#     age = serializers.IntegerField()
#     education = serializers.CharField()
#
#     class Meta:
#         model = Doctor
#         fields = (
#             "id",
#             "user",
#             "work_experience",
#             "age",
#             "education",
#             "category",
#             "timetable",
#         )
#
#     def update(self, instance, validated_data):
#         user = MyUser.objects.get(email=instance.user.email)
#         user_data = validated_data.get("user")
#         user_serializer = UserSerializer(user, data=user_data)
#         user_serializer.is_valid(raise_exception=True)
#         user_serializer.save()
#         instance.age = validated_data.get("age", instance.age)
#         instance.education = validated_data.get("education", instance.education)
#         instance.work_experience = validated_data.get(
#             "work_experience", instance.work_experience
#         )
#         category_data = validated_data.get("category")
#         category = DoctorsCategory.objects.get(name=category_data)
#         instance.category = category
#         timetable_data = validated_data.get("timetable")
#         timetable = TimeTable.objects.get(name=timetable_data)
#         instance.timetable = timetable
#         instance.save()
#
#         return instance
