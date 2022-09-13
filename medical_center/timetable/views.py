from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAdminUser
from timetable.models import TimeTable
from timetable.permissions import IsAdminDoctorSellerOrReadOnly
from timetable.serializers import TimeTableSerializer


class CreateTimeTableAPIView(generics.CreateAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
    permission_classes = [IsAdminDoctorSellerOrReadOnly]


class ListTimeTableAPIView(generics.ListAPIView):
    serializer_class = TimeTableSerializer
    permission_classes = [IsAdminDoctorSellerOrReadOnly]

    def get_queryset(self):
        return TimeTable.objects.all()


class UpdateDeleteTimeTableAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
    permission_classes = [IsAdminDoctorSellerOrReadOnly]
    lookup_field = "name"

    def get_object(self):
        name = self.kwargs.get("name")
        if not name:
            return NotFound
        return TimeTable.objects.filter(name=name).first()
