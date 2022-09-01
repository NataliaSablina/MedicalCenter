from django.urls import reverse
from rest_framework.test import APITestCase

from seller.models import Seller
from user.models import MyUser


# class SellerAPITestCase(APITestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         user4 = MyUser.objects.create_user(
#             email="user4@gmail.com",
#             first_name="user4",
#             second_name="user4",
#             sex="male",
#             phone_number="+48657823912",
#             date_of_birth="2003-12-06",
#             password="2",
#         )
#         print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
#         print(user4.pk)
#         seller1 = Seller.objects.create(
#             user=user4, work_experience="2", is_seller=True, age="18"
#         )
#         print("KKKKKKKKKKKKKKKKKKKKKKKKKKKK")
#         print(seller1.user.pk)
#
#     def test_all_sellers(self):
#         url = reverse('all-sellers')
#         response = self.client.get(url)
#         print(response.data)
#
#     @classmethod
#     def tearDownClass(cls):
#         super().tearDownClass()
#         MyUser.objects.all().delete()