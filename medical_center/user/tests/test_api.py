from collections import OrderedDict

from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase

from user.models import MyUser


class UserPageAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        call_command("loaddata", "fixtures/fixtures.json", verbosity=0)

    def test_user_page(self):
        url = reverse("user_page", args=["user4@gmail.com"])
        response = self.client.get(url)
        expected_data = [
            OrderedDict(
                [
                    ("id", 1),
                    ("last_login", None),
                    ("first_name", "user1"),
                    ("second_name", "user1"),
                    ("phone_number", "+48796730195"),
                    ("date_of_birth", "2003-12-06"),
                    ("sex", "male"),
                    ("photo", None),
                    ("email", "user4@gmail.com"),
                    ("is_active", True),
                    ("is_admin", False),
                ]
            )
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_registration(self):
        users_count = MyUser.objects.all().count()
        url = reverse("registration")
        response = self.client.post(
            url,
            data={
                "email": "user3@gmail.com",
                "first_name": "user3",
                "second_name": "user3",
                "sex": "male",
                "phone_number": "+48657823912",
                "date_of_birth": "2003-12-06",
                "password1": "3",
                "password2": "3",
            },
        )
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(MyUser.objects.all().count(), users_count + 1)

    def test_incorrect_registration_data(self):
        url = reverse("registration")
        response = self.client.post(
            url,
            data={
                "email": "user3@gmail.com",
                "first_name": "user3",
                "second_name": "user3",
                "phone_number": "+48657823912",
                "date_of_birth": "2003-12-06",
                "password1": "3",
                "password2": "2",
            },
        )
        incorrect_data_errors = {
            "3": ErrorDetail(string="Пароль не совпадает", code="invalid")
        }
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(incorrect_data_errors, response.data)
