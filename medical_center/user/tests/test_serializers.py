import datetime

from django.test import TestCase

from user.models import MyUser
from user.serializers import UserSerializer


# class UserSerializerTestCase(TestCase):
#     def test_ok(self):
#         user2 = MyUser.objects.create_user(email="user2@gmail.com",
#                                            first_name="user2",
#                                            second_name="user2",
#                                            sex="male",
#                                            phone_number="+48657823912",
#                                            date_of_birth='2003-12-06',
#                                            password='2')
#         serializer_data = UserSerializer(user2).data
#         expected_data = {
#             "id": user2.id,
#             "password": user2.password,
#             "last_login": user2.last_login,
#             "first_name": "user2",
#             "second_name": "user2",
#             "phone_number": "+48657823912",
#             "date_of_birth": user2.date_of_birth,
#             "sex": "male",
#             "creation_date": serializer_data["creation_date"],
#             "photo": user2.photo,
#             "email": user2.email,
#             "is_active": user2.is_active,
#             "is_admin": user2.is_admin,
#         }
#         # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
#         # print(serializer_data)
#         # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
#         # print(expected_data)
#         self.assertEqual(expected_data, serializer_data)
#
