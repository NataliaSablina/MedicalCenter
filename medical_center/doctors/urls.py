from django.urls import path, include

# from doctors.views import DoctorsCategoriesListAPIView, DoctorsCategoriesUpdateAPIView, DoctorsCategoriesDetailAPIView
from doctors.views import DoctorsCategoriesListAPIView, DoctorsCategoriesUpdateAPIView, \
    DoctorsCategoriesDestroyAPIView, DoctorsCategoriesAPIView
from rest_framework import routers

#
# router = routers.SimpleRouter()
# router.register(r'doctors_category_list', DoctorsCategoriesViewSet, basename='category')
# print(router.urls)

urlpatterns = [
    # path('categories/', include(router.urls)),
    path('categories/create/doctors/category/', DoctorsCategoriesListAPIView.as_view(), name='create-doctor-category'),
    path('categories/update/doctors/category/<int:pk>/', DoctorsCategoriesUpdateAPIView.as_view(), name='update-doctor-category'),
    path('categories/destroy/doctors/category/<int:pk>/', DoctorsCategoriesDestroyAPIView.as_view(), name='destroy-doctor-category'),
    path('categories/all/doctors/categories/', DoctorsCategoriesAPIView.as_view(), name='all-doctors-categories'),
    # path('categories/create/doctors/category/<int:pk>/', DoctorsCategoriesDetailAPIView.as_view(), name='create-doctor-category'),
    # path('categories/update/doctors/category/', UpdateDoctorCategory.as_view(), name='update-doctor-category'),
   # path('doctors_category_list/', DoctorsCategoriesListAPIView.as_view()),
   #  path('categories/doctors/categories/', DoctorsCategoriesViewSet.as_view({"get": "list"})),
   #  path('categories/update/doctors/category/<int:pk>/', DoctorsCategoriesListAPIView.as_view({"put": "update"})),
   #  path('categories/delete/doctors/category/<int:pk>/', DoctorsCategoriesListAPIView.as_view({"delete": "destroy"})),
   # path('doctors_category_list/<int:pk>/', DoctorsCategoriesUpdateAPIView.as_view()),
    # path('doctors_category_list/detail/<int:pk>/', DoctorsCategoriesDetailAPIView.as_view()),

]
