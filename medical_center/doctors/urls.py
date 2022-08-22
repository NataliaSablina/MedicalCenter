from django.urls import path, include

# from doctors.views import DoctorsCategoriesListAPIView, DoctorsCategoriesUpdateAPIView, DoctorsCategoriesDetailAPIView
from doctors.views import DoctorsCategoriesViewSet, CreateDoctorCategory
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'doctors_category_list', DoctorsCategoriesViewSet, basename='category')
print(router.urls)

urlpatterns = [
    path('categories/', include(router.urls)),
    path('categories/create/doctor/category/', CreateDoctorCategory.as_view(), name='create-doctor-category')
   # path('doctors_category_list/', DoctorsCategoriesListAPIView.as_view()),
   #  path('doctors_category_list/', DoctorsCategoriesViewSet.as_view({"get": "list"})),
   #  path('doctors_category_list/<int:pk>/',DoctorsCategoriesViewSet.as_view({"put": "update"})),
   # path('doctors_category_list/<int:pk>/', DoctorsCategoriesUpdateAPIView.as_view()),
    # path('doctors_category_list/detail/<int:pk>/', DoctorsCategoriesDetailAPIView.as_view()),

]
