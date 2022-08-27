from django.urls import path, include

from medicament.views import (
    MedicamentCategoryView,
    MedicamentCategoryListView,
    CurrentCategoryMedicamentListAPIView,
    CurrentMedicamentListAPIView,
)

urlpatterns = [
    path(
        "categories/all/medicament/categories/",
        MedicamentCategoryListView.as_view(),
        name="all-medicament-categories",
    ),
    path(
        "categories/create/medicament/category/",
        MedicamentCategoryView.as_view(),
        name="create-medicament-category",
    ),
    path(
        "categories/update/medicament/category/<str:title>/",
        MedicamentCategoryView.as_view(),
        name="update-medicament-category",
    ),
    path(
        "current/category/medicament/<str:title>/",
        CurrentCategoryMedicamentListAPIView.as_view(),
        name="current-category-medicament",
    ),
    path(
        "current/medicament/<str:title>/",
        CurrentMedicamentListAPIView.as_view(),
        name="current-medicament",
    ),
]
