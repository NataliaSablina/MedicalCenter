from collections import OrderedDict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user.models import MyUser

# email, first_name, second_name, sex, phone_number, date_of_birth, password=None
from user.serializers import UserSerializer


class UserPageAPITestCase(APITestCase):
    pass

    @classmethod
    def setUpClass(csl):
        super().setUpClass()
        user2 = MyUser.objects.create_user(
            email="user2@gmail.com",
            first_name="user2",
            second_name="user2",
            sex="male",
            phone_number="+48657823912",
            date_of_birth="2003-12-06",
        )

    def test_user_page(self):
        url = reverse("user-page", args=["user2@gmail.com"])
        response = self.client.get(url)
        expected_data = [
            OrderedDict(
                [
                    ("id", 3),
                    ("last_login", None),
                    ("first_name", "user2"),
                    ("second_name", "user2"),
                    ("phone_number", "+48657823912"),
                    ("date_of_birth", "2003-12-06"),
                    ("sex", "male"),
                    ("photo", None),
                    ("email", "user2@gmail.com"),
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
