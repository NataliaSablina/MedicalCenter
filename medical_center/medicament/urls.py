from django.urls import path, include

from medicament.views import (
    MedicamentCategoryView,
    MedicamentCategoryListView,
    CurrentCategoryMedicamentListAPIView,
    CurrentMedicamentListAPIView,
    MedicamentListAPIView,
    CreateMedicamentAPIView,
    UpdateMedicamentAPIView,
    CreateMedicamentCommentAPIView,
    UpdateDeleteMedicamentCommentAPIView,
    CurrentMedicamentCommentsAPIListView,
    CreateMedicamentSellerRelationsAPIView,
    UpdateDeleteMedicamentSellerRelationsAPIView,
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
    path(
        "all/medicament/",
        MedicamentListAPIView.as_view(),
        name="all-medicament",
    ),
    path(
        "create_medicament/",
        CreateMedicamentAPIView.as_view(),
        name="create_medicament",
    ),
    path(
        "update_medicament/<str:title>/",
        UpdateMedicamentAPIView.as_view(),
        name="update_medicament",
    ),
    path(
        "create_comment_medicament/",
        CreateMedicamentCommentAPIView.as_view(),
        name="create_comment_medicament",
    ),
    path(
        "update_delete_comment_medicament/<str:title>/",
        UpdateDeleteMedicamentCommentAPIView.as_view(),
        name="update_delete_comment_medicament",
    ),
    path(
        "current_medicament_comments/<str:title>/",
        CurrentMedicamentCommentsAPIListView.as_view(),
        name="current_medicament_comments",
    ),
    path(
        "create_medicament_seller_relations/",
        CreateMedicamentSellerRelationsAPIView.as_view(),
        name="create_medicament_seller_relations",
    ),
    path(
        "update_delete_medicament_seller_relations/<str:title>/",
        UpdateDeleteMedicamentSellerRelationsAPIView.as_view(),
        name="update_delete_medicament_seller_relations",
    ),
]
