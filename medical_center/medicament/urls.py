from django.urls import path, include

from medicament.views import MedicamentCategoryView, MedicamentCategoryListView

urlpatterns = [
    path('categories/all/medicament/categories/', MedicamentCategoryListView.as_view(), name='all-medicament-categories'),
    path('categories/create/medicament/category/', MedicamentCategoryView.as_view(), name='create-medicament-category'),
    path('categories/create/medicament/category/<int:pk>', MedicamentCategoryView.as_view(),
         name='update-medicament-category'),
]
