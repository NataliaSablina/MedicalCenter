import datetime

from django.core.management import call_command
from django.test import TestCase

from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
from user.models import MyUser
from user.serializers import UserSerializer


class DoctorsSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        call_command("loaddata", "fixtures/fixtures.json", verbosity=0)

    def test_get_timetable(self):
        doctor = Doctor.objects.get(user=4)
        serializer_data = DoctorSerializer(doctor).get_timetable(doctor)
        expected_data = "doctor doesn't have timetable"
        self.assertEqual(expected_data, serializer_data)
