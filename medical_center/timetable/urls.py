from django.urls import path, include

from timetable.views import CreateTimeTableAPIView, ListTimeTableAPIView, UpdateTimeTableAPIView

urlpatterns = [
    path('timetable_create/', CreateTimeTableAPIView.as_view(), name='timetable_create'),
    path('timetable_view/', ListTimeTableAPIView.as_view(), name='timetable_view'),
    path('timetable_update/<str:name>/', UpdateTimeTableAPIView.as_view(), name='timetable_update'),
]
