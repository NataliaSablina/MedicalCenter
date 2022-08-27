import os

from django.test import TestCase

from user.utils import sex_control


class UtilsTestCase(TestCase):
    def test_sex_control_false(self):
        result = sex_control("f")
        self.assertEqual(False, result)

    def test_sex_control_true_male(self):
        result = sex_control("male")
        self.assertEqual(True, result)

    def test_sex_control_true_female(self):
        result = sex_control("female")
        self.assertEqual(True, result)
