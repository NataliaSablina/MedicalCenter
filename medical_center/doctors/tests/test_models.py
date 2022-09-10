from django.core.management import call_command
from django.test import TestCase

from doctors.models import DoctorsCategory, Doctor, CommentDoctor


class TestDoctorsModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        call_command("loaddata", "fixtures/fixtures.json", verbosity=0)

    def test_str_doctors_category(self):
        category1 = DoctorsCategory.objects.get(name="category3")
        expected_data = category1.name
        self.assertEqual(expected_data, str(category1))

    def test_str_doctor(self):
        doctor = Doctor.objects.get(user=1)
        expected_data = doctor.user.email
        self.assertEqual(expected_data, str(doctor))

    def test_str_comment_doctor(self):
        comment = CommentDoctor.objects.get(title="doctor1comment1")
        expected_data = comment.title
        self.assertEqual(expected_data, str(comment))
