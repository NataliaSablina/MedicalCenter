from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from timetable.models import TimeTable
from timetable.permissions import IsAdminAndDoctorOrReadOnly
from timetable.serializers import TimeTableSerializer


class CreateTimeTableAPIView(generics.CreateAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
    permission_classes = [IsAdminAndDoctorOrReadOnly]


class ListTimeTableAPIView(generics.ListAPIView):
    serializer_class = TimeTableSerializer
    permission_classes = [IsAdminAndDoctorOrReadOnly]

    def get_queryset(self):
        return TimeTable.objects.select_related("user")


class UpdateTimeTableAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TimeTableSerializer
    permission_classes = [IsAdminAndDoctorOrReadOnly]
    lookup_field = "name"

    def get_queryset(self):
        name = self.kwargs.get("name")
        if not name:
            return TimeTable.objects.all()
        return TimeTable.objects.filter(name=name)
