from django.db.models import Prefetch
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from doctors.models import DoctorsCategory, Doctor, CommentDoctor
from doctors.serializers import (
    DoctorsCategorySerializer,
    DoctorSerializer,
    RegistrationDoctorSerializer,
    CommentDoctorSerializer,
    DoctorUpdateSerializer,
)


class DoctorsCategoriesListAPIView(generics.ListCreateAPIView):
    queryset = DoctorsCategory.objects.all()
    serializer_class = DoctorsCategorySerializer
    permission_classes = [
        IsAdminUser,
    ]


class DoctorsCategoriesUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = DoctorsCategory.objects.all()
    serializer_class = DoctorsCategorySerializer
    permission_classes = [
        IsAdminUser,
    ]


class CreateCommentDoctorAPIView(generics.CreateAPIView):
    queryset = CommentDoctor.objects.all()
    serializer_class = CommentDoctorSerializer


class UpdateCommentDoctorAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentDoctorSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "title"

    def get_queryset(self):
        title = self.kwargs.get("title")
        if not title:
            return CommentDoctor.objects.all()
        return CommentDoctor.objects.filter(title=title)

    def get_object(self):
        title = self.kwargs.get("title")
        print(title)
        instance = (
            CommentDoctor.objects.select_related("user").filter(title=title).first()
        )
        print(instance)
        if not instance:
            raise NotFound
        return instance


class DoctorCommentListAPIView(generics.ListAPIView):
    serializer_class = CommentDoctorSerializer
    lookup_url_kwarg = "email"

    def get_queryset(self):
        title = self.kwargs.get(self.lookup_url_kwarg)
        if not title:
            return CommentDoctor.objects.all()
        return CommentDoctor.objects.filter(doctor__user__email=title)


class DoctorsCategoriesDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = DoctorsCategory.objects.all()
    serializer_class = DoctorsCategorySerializer
    permission_classes = [
        IsAdminUser,
    ]


class DoctorsCategoriesAPIView(generics.ListAPIView):
    queryset = DoctorsCategory.objects.all()
    serializer_class = DoctorsCategorySerializer


class CurrentCategoryDoctorListAPIView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        name = self.kwargs.get("name")
        doctors = Doctor.objects.filter(category__name=name)
        return doctors


class CurrentDoctorListAPIView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        email = self.kwargs.get("email")
        return (
            Doctor.objects.select_related("user")
            .prefetch_related("timetable")
            .filter(user__email=email)
        )
        # return Doctor.objects.filter(user__email=email)


class RegistrationDoctorAPIView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = RegistrationDoctorSerializer
    permission_classes = [IsAdminUser]


class UpdateDoctorAPIView(generics.RetrieveUpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorUpdateSerializer
    lookup_url_kwarg = "email"

    def get_object(self):
        email = self.kwargs.get(self.lookup_url_kwarg)
        instance = (
            Doctor.objects.select_related("user")
            .prefetch_related("timetable")
            .filter(user__email=email)
            .first()
        )
        if not instance:
            raise NotFound
        return instance

    def put(self, request, *args, **kwargs):
        doctor = Doctor.objects.select_related("user").get(
            user__email=kwargs.get("email", None)
        )
        serializer = DoctorUpdateSerializer(instance=doctor, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        serializer.save()
        return Response({"post": serializer.data})


class DoctorsListAPIView(generics.ListAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Doctor.objects.select_related("user")
