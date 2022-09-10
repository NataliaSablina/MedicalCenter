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
from user.models import MyUser


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
        doctors = Doctor.objects.filter(category__name=name)
        return doctors


class CurrentDoctorListAPIView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        email = self.kwargs.get("email")
        return Doctor.objects.select_related("user").prefetch_related("user__doctor_timetable").filter(
            user__email=email)
        # return Doctor.objects.filter(user__email=email)


class RegistrationDoctorAPIView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = RegistrationDoctorSerializer
    permission_classes = [IsAdminUser]


class UpdateDoctorAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = DoctorUpdateSerializer
    lookup_url_kwarg = "email"

    # def get_queryset(self):
    #     email = self.kwargs.get(self.lookup_url_kwarg)
    #     if not email:
    #         return Doctor.objects.all()
    #     return Doctor.objects.filter(user__email=email)

    def get_object(self):
        print('KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK')
        email = self.kwargs.get(self.lookup_url_kwarg)
        instance = Doctor.objects.filter(user__email=email).first()
        if not instance:
            raise NotFound
        return instance

    def put(self, request, *args, **kwargs):
        # doctor = self.get_object()
        print('YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
        # doctor = self.get_object()
        doctor = Doctor.objects.select_related('user').get(user__email=kwargs.get('email', None))
        serializer = DoctorUpdateSerializer(instance=doctor, data=request.data)
        print('AAAAAAAAAAAAa')
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        self.perform_update(serializer)
        print(serializer.data)
        return Response({"post": serializer.data})
    #     # print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPp")
    #     # if serializer.is_valid():
    #     #     print(
    #     #         "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    #     #     )
    #     #     serializer.save()
    #     #     return Response(serializer.data)
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     # print(serializer.errors)
    #     # print(')))))))))))))))))))))))))))))))))))))))))))))))))))))')
    #     # # self.perform_update(serializer)
    #     # print(serializer.data)
    #     # return HttpResponse('hi')


class DoctorsListAPIView(generics.ListAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Doctor.objects.select_related("user")
