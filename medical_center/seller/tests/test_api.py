from collections import OrderedDict
import datetime
from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SellerAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        call_command("loaddata", "user/fixtures.json", verbosity=0)

    def test_all_sellers(self):
        url = reverse("all-sellers")
        response = self.client.get(url)
        expected_data = [
            OrderedDict(
                [
                    ("id", 1),
                    ("first_name", "user5"),
                    ("second_name", "user5"),
                    ("phone_number", "+48796730195"),
                    ("sex", "male"),
                    ("date_of_birth", datetime.date(2003, 12, 6)),
                    ("email", "user5@gmail.com"),
                    ("work_experience", "SELLER"),
                    ("age", 18),
                    ("is_seller", True),
                    ("user", 2),
                ]
            )
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)
