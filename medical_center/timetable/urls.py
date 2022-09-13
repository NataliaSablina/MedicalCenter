from django.urls import path, include

from timetable.views import (
    CreateTimeTableAPIView,
    ListTimeTableAPIView,
    UpdateDeleteTimeTableAPIView,
)

urlpatterns = [
    path(
        "timetable_create/", CreateTimeTableAPIView.as_view(), name="timetable_create"
    ),
    path("timetable_view/", ListTimeTableAPIView.as_view(), name="timetable_view"),
    path(
        "timetable_update_delete/<str:name>/",
        UpdateDeleteTimeTableAPIView.as_view(),
        name="timetable_update_delete",
    ),
]
