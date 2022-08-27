from rest_framework import serializers
from doctors.models import DoctorsCategory, Doctor


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


# class DoctorsCategorySerializer(serializers.Serializer):
#     name = serializers.CharField()
#
#     def create(self, validated_data):
#         return DoctorsCategory.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.save()
#         return instance
