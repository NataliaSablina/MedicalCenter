from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from timetable.models import TimeTable
from timetable.permissions import IsAdminAndDoctorOrReadOnly
from timetable.serializers import TimeTableSerializer


class CreateTimeTable(generics.ListCreateAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
    permission_classes = [IsAdminAndDoctorOrReadOnly]
