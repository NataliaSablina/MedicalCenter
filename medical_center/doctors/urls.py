from django.urls import path, include

from doctors.views import (
    DoctorsCategoriesListAPIView,
    DoctorsCategoriesUpdateAPIView,
    DoctorsCategoriesDestroyAPIView,
    DoctorsCategoriesAPIView,
    CurrentCategoryDoctorListAPIView,
    CurrentDoctorListAPIView,
    RegistrationDoctorAPIView,
    DoctorsListAPIView, CreateCommentDoctorAPIView, UpdateCommentDoctorAPIView, DoctorCommentListAPIView,
)


urlpatterns = [
    path(
        "categories/create/doctors/category/",
        DoctorsCategoriesListAPIView.as_view(),
        name="create-doctor-category",
    ),
    path(
        "categories/update/doctors/category/<int:pk>/",
        DoctorsCategoriesUpdateAPIView.as_view(),
        name="update-doctor-category",
    ),
    path(
        "categories/destroy/doctors/category/<int:pk>/",
        DoctorsCategoriesDestroyAPIView.as_view(),
        name="destroy-doctor-category",
    ),
    path(
        "categories/all/doctors/categories/",
        DoctorsCategoriesAPIView.as_view(),
        name="all-doctors-categories",
    ),
    path(
        "current/category/doctors/<str:name>/",
        CurrentCategoryDoctorListAPIView.as_view(),
        name="current-category-doctors",
    ),
    path(
        "current/doctor/<str:email>/",
        CurrentDoctorListAPIView.as_view(),
        name="current-doctor",
    ),
    path("create_doctor/", RegistrationDoctorAPIView.as_view(), name="create_doctor"),
    path("all_doctors/", DoctorsListAPIView.as_view(), name="all_doctors"),
    path("create_comment_doctor/", CreateCommentDoctorAPIView.as_view(), name="create_comment_doctor"),
    path("update_comment_doctor/<str:title>/", UpdateCommentDoctorAPIView.as_view(), name="update_comment_doctor"),
    path("comments_doctor/<str:email>/", DoctorCommentListAPIView.as_view(), name="comments_doctor"),
]
