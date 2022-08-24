from rest_framework import serializers

from medicament.models import MedicamentCategory


class MedicamentCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicamentCategory
        fields = '__all__'


class MedicamentCategorySerializer(serializers.Serializer):
    title = serializers.CharField()

    def create(self, validated_data):
        return MedicamentCategory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        return instance

