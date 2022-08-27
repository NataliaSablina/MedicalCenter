from collections import OrderedDict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from medicament.models import MedicamentCategory, Medicament, MedicamentSellerRelations
from medicament.serializers import MedicamentCategorySerializer, MedicamentSerializer
from seller.models import Seller
from user.models import MyUser


class MedicamentCategoryAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.category1 = MedicamentCategory.objects.create(title="Therapists1")
        self.category2 = MedicamentCategory.objects.create(title="Therapists2")
        self.medicament1 = Medicament.objects.create(title='medicament1',
                                                     instruction='medicament1',
                                                     brief_instruction='medicament1',
                                                     category=self.category1)
        self.user2 = MyUser.objects.create_user(email="user2@gmail.com",
                                                first_name="user2",
                                                second_name="user2",
                                                sex="male",
                                                phone_number="+48657823912",
                                                date_of_birth='2003-12-06',
                                                password='2')
        self.seller1 = Seller.objects.create(user=self.user2,
                                             work_experience="2",
                                             is_seller=True,
                                             age='18')
        self.msrelations = MedicamentSellerRelations.objects.create(medicament=self.medicament1,
                                                                    seller=self.seller1,
                                                                    price=(14, 'USD'))

    def test_all_medicament_categories(self):
        url = reverse('all-medicament-categories')
        response = self.client.get(url)
        expected_data = [OrderedDict([('title', 'Therapists1')]), OrderedDict([('title', 'Therapists2')])]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_current_category(self):
        url = reverse('current-category-medicament', args=[self.category1.title])
        response = self.client.get(url)
        expected_data =[OrderedDict([('id', 2),
                                     ('seller', 'user2@gmail.com'),
                                     ('medicament', 'medicament1'),
                                     ('brief_instruction', 'medicament1'),
                                     ('instruction', 'medicament1'),
                                     ('title', 'medicament1'),
                                     ('category', 'Therapists1'),
                                     ('price_currency', 'USD'),
                                     ('price', '14.00')])]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)
