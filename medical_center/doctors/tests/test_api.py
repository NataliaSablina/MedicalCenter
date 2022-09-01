import datetime
from collections import OrderedDict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from doctors.models import DoctorsCategory, Doctor
from user.models import MyUser


class DoctorsViewAPI(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category1 = DoctorsCategory.objects.create(name="doctors1")
        cls.category2 = DoctorsCategory.objects.create(name="doctors2")
        cls.user2 = MyUser.objects.create_user(
            email="user2@gmail.com",
            first_name="user2",
            second_name="user2",
            sex="male",
            phone_number="+48657823912",
            date_of_birth="2003-12-06",
            password="2",
        )
        print('YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
        print(cls.user2.pk)
        cls.doctor1 = Doctor.objects.create(
            user=cls.user2,
            category=cls.category1,
            work_experience="2",
            education="3",
            age=23,
            is_doctor=True,
        )
        print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
        print(cls.doctor1.user.pk)

    def test_all_doctors_categories(self):
        url = reverse("all-doctors-categories")
        response = self.client.get(url)
        print(response.data)
        expected_data = [
            OrderedDict([("id", 1), ("name", "doctors1")]),
            OrderedDict([("id", 2), ("name", "doctors2")]),
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_current_category(self):
        url = reverse("current-category-doctors", args=["doctors1"])
        response = self.client.get(url)
        expected_data = [
            OrderedDict(
                [
                    ("id", 1),
                    ("first_name", "user2"),
                    ("second_name", "user2"),
                    ("phone_number", "+48657823912"),
                    ("sex", "male"),
                    ("date_of_birth", datetime.date(2003, 12, 6)),
                    ("email", "user2@gmail.com"),
                    ("work_experience", "2"),
                    ("education", "3"),
                    ("age", 23),
                    ("is_doctor", True),
                    ("user", 1),
                    ("category", 1),
                ]
            )
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_current_doctor(self):
        url = reverse("current-doctor", args=["user2@gmail.com"])
        response = self.client.get(url)
        print(response.data)
        expected_data = [
            OrderedDict(
                [
                    ("id", 1),
                    ("first_name", "user2"),
                    ("second_name", "user2"),
                    ("phone_number", "+48657823912"),
                    ("sex", "male"),
                    ("date_of_birth", datetime.date(2003, 12, 6)),
                    ("email", "user2@gmail.com"),
                    ("work_experience", "2"),
                    ("education", "3"),
                    ("age", 23),
                    ("is_doctor", True),
                    ("user", 1),
                    ("category", 1),
                ]
            )
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    # def tearDownClass(self):
    #     result1 = MyUser.objects.get(email='user2@gmail.com')
    #     print(result1)
    #     result1.delete()
    #     result = MyUser.objects.get(email='user2@gmail.com')
    #     print(result)

