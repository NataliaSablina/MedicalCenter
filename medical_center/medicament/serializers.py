from rest_framework import serializers

from medicament.models import MedicamentCategory, Medicament, MedicamentSellerRelations


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

#
# class MedicamentModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Medicament
#         fields = '__all__'


class MedicamentSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()
    medicament = serializers.SerializerMethodField()
    brief_instruction = serializers.SerializerMethodField()
    instruction = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = MedicamentSellerRelations
        fields = '__all__'

    def get_instruction(self, instance):
        return instance.medicament.instruction

    def get_medicament(self, instance):
        return instance.medicament.title

    def get_seller(self, instance):
        return instance.seller.user.email

    def get_brief_instruction(self, instance):
        return instance.medicament.brief_instruction

    def get_title(self, instance):
        return instance.medicament.title

    def get_category(self, instance):
        return instance.medicament.category.title




