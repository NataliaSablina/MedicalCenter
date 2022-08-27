from collections import OrderedDict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user.models import MyUser

# email, first_name, second_name, sex, phone_number, date_of_birth, password=None
from user.serializers import UserSerializer


class UserPageAPITestCase(APITestCase):
    pass
    # def test_user_page(self):
    #     user2 = MyUser.objects.create_user(email="user2@gmail.com",
    #                                        first_name="user2",
    #                                        second_name="user2",
    #                                        sex="male",
    #                                        phone_number="+48657823912",
    #                                        date_of_birth='2003-12-06',
    #                                        password='2')
    #     url = reverse('user-page', args=['user2@gmail.com'])
    #     response = self.client.get(url)
    #     serializer_data = UserSerializer(user2).data
    #     print(response.data)
    #     print("___________________________")
    #     print(serializer_data)
    #     user2_data = [OrderedDict([('id', 1), ('password', 'pbkdf2_sha256$390000$JO8BpAB2DvJHz1nIRUj9d6$WXT9C70eiZCx6XCTgJdIwKhq6TcZ/sry2Vi4lj5DFTM='), ('last_login', None), ('first_name', 'user2'),
    #                                ('second_name', "user2"),('phone_number', '+48657823912'), ('date_of_birth', '2003-12-06'), ('sex', 'male'), ('creation_date', '2022-08-27T09:03:59.833876Z'), ('photo', None), ('email', 'user2@gmail.com'), ('is_active', True), ('is_admin', False)])]
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     self.assertEqual(user2_data, response.data)
