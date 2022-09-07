from collections import OrderedDict

from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class MedicamentCategoryAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        call_command("loaddata", "user/fixtures.json", verbosity=0)

    def test_all_medicament_categories(self):
        url = reverse("all-medicament-categories")
        response = self.client.get(url)
        expected_data = [
            OrderedDict([("title", "category3")]),
            OrderedDict([("title", "category4")]),
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_current_category(self):
        url = reverse("current-category-medicament", args=["category3"])
        response = self.client.get(url)
        expected_data = [
            OrderedDict(
                [
                    ("id", 1),
                    ("seller", "user5@gmail.com"),
                    ("medicament", "medicament1"),
                    ("brief_instruction", "medicament1 brief_instruction"),
                    ("instruction", "medicament1 instruction"),
                    ("title", "medicament1"),
                    ("category", "category3"),
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
                    ("seller", "user5@gmail.com"),
                    ("medicament", "medicament1"),
                    ("brief_instruction", "medicament1 brief_instruction"),
                    ("instruction", "medicament1 instruction"),
                    ("title", "medicament1"),
                    ("category", "category3"),
                    ("price_currency", "USD"),
                    ("price", "14.00"),
                ]
            )
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    #
    # # def test_medicament_category_post(self):
    # """работа с правами доступа добавить"""
    # #     categories_count = MedicamentCategory.objects.all().count()
    # #     url = reverse('create-medicament-category')
    # #     response = self.client.post(url, data={'title': 'gleb'})
    # #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    # #     self.assertEqual(MedicamentCategory.objects.all().count(), categories_count + 1)
    #
