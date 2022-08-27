from django.test import TestCase

from user.utils import sex_control


class UtilsTestCase(TestCase):
    def test_sex_control_false(self):
        result = sex_control("f")
        self.assertEqual(False, result)
