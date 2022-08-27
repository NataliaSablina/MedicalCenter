from collections import OrderedDict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from medicament.models import MedicamentCategory, Medicament, MedicamentSellerRelations
from seller.models import Seller
from user.models import MyUser


class MedicamentCategoryAPITestCase(APITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        category1 = MedicamentCategory.objects.create(title="Therapists1")
        category2 = MedicamentCategory.objects.create(title="Therapists2")
        medicament1 = Medicament.objects.create(
            title="medicament1",
            instruction="medicament1",
            brief_instruction="medicament1",
            category=category1,
        )
        user2 = MyUser.objects.create_user(
            email="user2@gmail.com",
            first_name="user2",
            second_name="user2",
            sex="male",
            phone_number="+48657823912",
            date_of_birth="2003-12-06",
            password="2",
        )
        seller1 = Seller.objects.create(
            user=user2, work_experience="2", is_seller=True, age="18"
        )
        msrelations = MedicamentSellerRelations.objects.create(
            medicament=medicament1, seller=seller1, price=(14, "USD")
        )

    def test_all_medicament_categories(self):
        url = reverse("all-medicament-categories")
        response = self.client.get(url)
        expected_data = [
            OrderedDict([("title", "Therapists1")]),
            OrderedDict([("title", "Therapists2")]),
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_current_category(self):
        url = reverse("current-category-medicament", args=["Therapists1"])
        response = self.client.get(url)
        expected_data = [
            OrderedDict(
                [
                    ("id", 1),
                    ("seller", "user2@gmail.com"),
                    ("medicament", "medicament1"),
                    ("brief_instruction", "medicament1"),
                    ("instruction", "medicament1"),
                    ("title", "medicament1"),
                    ("category", "Therapists1"),
                    ("price_currency", "USD"),
                    ("price", "14.00"),
                ]
            )
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

    def test_current_medicament(self):
        url = reverse("current-medicament", args=["medicament1"])
        response = self.client.get(url)
        expected_data = [
            OrderedDict(
                [
                    ("id", 1),
                    ("seller", "user2@gmail.com"),
                    ("medicament", "medicament1"),
                    ("brief_instruction", "medicament1"),
                    ("instruction", "medicament1"),
                    ("title", "medicament1"),
                    ("category", "Therapists1"),
                    ("price_currency", "USD"),
                    ("price", "14.00"),
                ]
            )
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    # def test_medicament_category_post(self):
    """работа с правами доступа добавить"""
    #     categories_count = MedicamentCategory.objects.all().count()
    #     url = reverse('create-medicament-category')
    #     response = self.client.post(url, data={'title': 'gleb'})
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(MedicamentCategory.objects.all().count(), categories_count + 1)
