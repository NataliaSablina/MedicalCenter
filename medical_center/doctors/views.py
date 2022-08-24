from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAdminUser
from doctors.models import DoctorsCategory, Doctor
from doctors.serializers import DoctorsCategorySerializer, DoctorSerializer


class DoctorsCategoriesListAPIView(generics.ListCreateAPIView):
    queryset = DoctorsCategory.objects.all()
    serializer_class = DoctorsCategorySerializer
    permission_classes = [IsAdminUser, ]


class DoctorsCategoriesUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = DoctorsCategory.objects.all()
    serializer_class = DoctorsCategorySerializer
    permission_classes = [IsAdminUser, ]


class DoctorsCategoriesDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = DoctorsCategory.objects.all()
    serializer_class = DoctorsCategorySerializer
    permission_classes = [IsAdminUser, ]


class DoctorsCategoriesAPIView(generics.ListAPIView):
    queryset = DoctorsCategory.objects.all()
    serializer_class = DoctorsCategorySerializer


class CurrentCategoryDoctorListAPIView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        print(pk)
        print(Doctor.objects.filter(category__id=pk))
        return Doctor.objects.filter(category__id=pk)


class CurrentDoctorListAPIView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Doctor.objects.filter(pk=pk)












#
# class DoctorsCategoriesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = DoctorsCategory.objects.all()
#     serializer_class = DoctorsCategorySerializer








# class DoctorsCategoriesViewSet(viewsets.ModelViewSet):
#     # queryset = DoctorsCategory.objects.all()
#     serializer_class = DoctorsCategorySerializer
#     # permission_classes =  [IsAUthenticatedOnly]
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return DoctorsCategory.objects.all()
#         return DoctorsCategory.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=False)
#     def category(self, request):
#         cats = DoctorsCategory.objects.all()
#         return Response({'cats': [c.name for c in cats]})

    # @action(methods=['post'], detail=True)
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# class CreateDoctorCategory(generics.CreateAPIView):
#     queryset = DoctorsCategory.objects.all()
#     serializer_class = DoctorsCategorySerializer
#     permission_classes = [IsAdminUser, ]
#
#
# class UpdateDoctorCategory(generics.UpdateAPIView):
#     queryset = DoctorsCategory.objects.all()
#     serializer_class = DoctorsCategorySerializer
#     permission_classes = [IsAdminUser, ]

# class DoctorsCategoriesListAPIView(generics.ListCreateAPIView):
#     queryset = DoctorsCategory.objects.all()
#     serializer_class = DoctorsCategorySerializer
#
#
# class DoctorsCategoriesUpdateAPIView(generics.UpdateAPIView):
#     queryset = DoctorsCategory.objects.all()
#     serializer_class = DoctorsCategorySerializer
#
#
# class DoctorsCategoriesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = DoctorsCategory.objects.all()
#     serializer_class = DoctorsCategorySerializer

#
# class DoctorsCategoriesListAPIView(APIView):
#     # def get(self, request, pk):
#     #     categories = DoctorsCategory.objects.all().values('id', 'name')
#     #     print(categories)
#     #     return Response({'categories': DoctorsCategorySerializer(categories, many=True).data})
#     permission_classes = [IsAdminUser, ]
#
#     def post(self, request):
#         serializer = DoctorsCategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'category': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"Metod PUT not allowed"})
#         try:
#             instance = DoctorsCategory.objects.get(pk=pk)
#         except:
#             return Response({"error: object doesn't exists"})
#
#         serializer = DoctorsCategorySerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post":serializer.data})
#
#     def delete(self, reguest, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"Metod DELETE not allowed"})
#         try:
#             instance = DoctorsCategory.objects.delete(pk=pk)
#         except:
#             return Response({"error: object doesn't exists"})
#         instance.delete()
#         return Response({'post': "deleted" + str(pk)})