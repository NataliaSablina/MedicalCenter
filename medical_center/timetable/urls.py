from django.urls import path, include

from timetable.views import CreateTimeTable

urlpatterns = [
    path('timetable_view/', CreateTimeTable.as_view(), name='timetable_view')
]
