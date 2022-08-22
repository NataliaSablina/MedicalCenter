from rest_framework import serializers
from doctors.models import DoctorsCategory


class DoctorsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsCategory
        fields = "__all__"


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

