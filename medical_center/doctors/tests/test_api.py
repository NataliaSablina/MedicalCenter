import datetime
from collections import OrderedDict
from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class DoctorsViewAPI(APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        call_command("loaddata", "fixtures/fixtures.json", verbosity=0)

    def test_all_doctors_categories(self):
        url = reverse("all-doctors-categories")
        response = self.client.get(url)
        expected_data = [
            OrderedDict([("id", 1), ("name", "category3")]),
            OrderedDict([("id", 2), ("name", "category4")]),
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_current_category(self):
        url = reverse("current-category-doctors", args=["category4"])
        response = self.client.get(url)
        expected_data = [
            OrderedDict(
                [
                    ("id", 1),
                    ("first_name", "user1"),
                    ("second_name", "user1"),
                    ("phone_number", "+48796730195"),
                    ("sex", "male"),
                    ("date_of_birth", datetime.date(2003, 12, 6)),
                    ("email", "user4@gmail.com"),
                    ("timetable", "doctor doesn't have timetable"),
                    ("work_experience", "MED"),
                    ("education", "BSU"),
                    ("age", 18),
                    ("is_doctor", True),
                    ("user", 1),
                    ("category", 2),
                ]
            )
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_current_doctor(self):
        url = reverse("current-doctor", args=["user4@gmail.com"])
        response = self.client.get(url)
        expected_data = [
            OrderedDict(
                [
                    ("id", 1),
                    ("first_name", "user1"),
                    ("second_name", "user1"),
                    ("phone_number", "+48796730195"),
                    ("sex", "male"),
                    ("date_of_birth", datetime.date(2003, 12, 6)),
                    ("email", "user4@gmail.com"),
                    ("timetable", "doctor doesn't have timetable"),
                    ("work_experience", "MED"),
                    ("education", "BSU"),
                    ("age", 18),
                    ("is_doctor", True),
                    ("user", 1),
                    ("category", 2),
                ]
            )
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)
