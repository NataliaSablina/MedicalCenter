from django.db import models
from seller.models import Seller
from user.models import MyUser
from djmoney.models.fields import MoneyField


class MedicamentCategory(models.Model):
    title = models.CharField(verbose_name="title", max_length=250)

    class Meta:
        verbose_name = "MedicamentCategory"
        verbose_name_plural = "MedicamentCategory"
        db_table = "MedicamentCategories"

    def __str__(self):
        return f"{self.title}, {self.pk}"


class Medicament(models.Model):
    title = models.CharField(verbose_name="title", max_length=250)
    instruction = models.TextField(verbose_name="instruction")
    brief_instruction = models.TextField(verbose_name="brief_instruction")
    category = models.ForeignKey(
        MedicamentCategory, on_delete=models.CASCADE, verbose_name="category"
    )

    class Meta:
        verbose_name = "Medicament"
        verbose_name_plural = "Medicaments"
        db_table = "Medicament"

    def __str__(self):
        return self.title


class CommentMedicament(models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.SET_NULL, verbose_name="user", null=True
    )
    content = models.TextField(verbose_name="content")
    creation_date = models.DateField(
        verbose_name="creation_date", auto_now_add=True, auto_now=False
    )

    class Meta:
        verbose_name = "CommentMedicament"
        verbose_name_plural = "CommentsMedicament"
        db_table = "CommentMedicament"

    def __str__(self):
        return self.pk, self.content[:20]


class MedicamentSellerRelations(models.Model):
    price = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        verbose_name="seller",
        related_name="seller_relations",
    )
    medicament = models.ForeignKey(
        Medicament, on_delete=models.CASCADE, verbose_name="medicament"
    )

    class Meta:
        verbose_name = "MedicamentSellerRelations"
        verbose_name_plural = "MedicamentSellerRelations"
        db_table = "MedicamentSellerRelations"

    def __str__(self):
        return f"{self.medicament.title}, {self.seller.user.first_name}, {self.price}"
