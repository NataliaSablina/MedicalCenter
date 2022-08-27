from rest_framework import serializers
from doctors.models import Doctor
from user.models import MyUser


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = MyUser
        fields = [
            'email', 'first_name', 'second_name', 'sex', 'phone_number', 'date_of_birth', 'password1', 'password2'
        ]

    def save(self, *args, **kwargs):
        user = MyUser.objects.create_user(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            second_name=self.validated_data['second_name'],
            sex=self.validated_data['sex'],
            phone_number=self.validated_data['phone_number'],
            date_of_birth=self.validated_data['date_of_birth']
        )
        password1 = self.validated_data['password1']
        password2 = self.validated_data['password2']
        if password1 != password2:
            raise serializers.ValidationError({password1: "Пароль не совпадает"})
        user.set_password(password1)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

