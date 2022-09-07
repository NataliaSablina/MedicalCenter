from rest_framework import generics, status
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
        print(name)
        doctors = Doctor.objects.filter(category__name=name)
        return doctors


class CurrentDoctorListAPIView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        email = self.kwargs.get("email")
        return Doctor.objects.filter(user__email=email)


class RegistrationDoctorAPIView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = RegistrationDoctorSerializer
    permission_classes = [IsAdminUser]


class UpdateDoctorAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = DoctorSerializer
    lookup_url_kwarg = "email"

    def get_queryset(self):
        email = self.kwargs.get(self.lookup_url_kwarg)
        if not email:
            return Doctor.objects.all()
        return Doctor.objects.filter(user__email=email)

    def put(self, request, *args, **kwargs):
        serializer = DoctorUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorsListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAdminUser]
