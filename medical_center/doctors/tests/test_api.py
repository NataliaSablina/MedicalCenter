import datetime
from collections import OrderedDict
from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from doctors.models import Doctor
from doctors.views import RegistrationDoctorAPIView, UpdateCommentDoctorAPIView
from user.models import MyUser


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
                    (
                        "timetable",
                        {
                            "monday": "7.30a.m-2p.m",
                            "tuesday": "7.30a.m-2p.m",
                            "wednesday": "7.30a.m-2p.m",
                            "thursday": "7.30a.m-2p.m",
                            "friday": "7.30a.m-2p.m",
                            "saturday": "7.30a.m-2p.m",
                            "sunday": "7.30a.m-2p.m",
                        },
                    ),
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
                    (
                        "timetable",
                        {
                            "monday": "7.30a.m-2p.m",
                            "tuesday": "7.30a.m-2p.m",
                            "wednesday": "7.30a.m-2p.m",
                            "thursday": "7.30a.m-2p.m",
                            "friday": "7.30a.m-2p.m",
                            "saturday": "7.30a.m-2p.m",
                            "sunday": "7.30a.m-2p.m",
                        },
                    ),
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

    def test_registration(self):
        users_count = Doctor.objects.all().count()
        user = MyUser.objects.get(pk=5)
        factory = APIRequestFactory()
        url = reverse("create_doctor")
        request = factory.post(
            url,
            data={
                "email": "doctor2@gmail.com",
                "first_name": "doctor2",
                "second_name": "doctor2",
                "sex": "male",
                "phone_number": "+48657823912",
                "date_of_birth": "2003-12-06",
                "password1": "3",
                "password2": "3",
                "age": 23,
                "work_experience": "5 years",
                "education": "BSU",
                "category": 2,
                "is_doctor": True,
            },
            format="json",
        )
        force_authenticate(request, user=user)
        view = RegistrationDoctorAPIView.as_view()
        response = view(request)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(Doctor.objects.all().count(), users_count + 1)

    def test_registration_error(self):
        user = MyUser.objects.get(pk=5)
        factory = APIRequestFactory()
        url = reverse("create_doctor")
        request = factory.post(
            url,
            data={
                "email": "doctor2@gmail.com",
                "first_name": "doctor2",
                "second_name": "doctor2",
                "sex": "male",
                "phone_number": "+48657823912",
                "date_of_birth": "2003-12-06",
                "password1": "3",
                "password2": "2",
                "age": 23,
                "work_experience": "5 years",
                "education": "BSU",
                "category": 2,
                "is_doctor": True,
            },
            format="json",
        )
        force_authenticate(request, user=user)
        view = RegistrationDoctorAPIView.as_view()
        response = view(request)
        incorrect_data_errors = {
            "3": ErrorDetail(string="Пароль не совпадает", code="invalid")
        }
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(incorrect_data_errors, response.data)

    # def test_update_comment(self):
    #     user = MyUser.objects.get(pk=5)
    #     factory = APIRequestFactory()
    #     url = reverse("update_comment_doctor", args=["doctor1comment1"])
    #     print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
    #     print(url)
    #     request = factory.put(url, data={
    #         "content": "content for doctor1comment12322"
    #     })
    #     force_authenticate(request, user=user)
    #     print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPp')
    #     view = UpdateCommentDoctorAPIView.as_view()
    #     print(view.initkwargs)
    #     print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPp')
    #
    #     response = view(request)
    #     print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPp')
    #
    #     print(response.status_code)
