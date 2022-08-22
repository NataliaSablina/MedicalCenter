from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from doctors.models import DoctorsCategory
from doctors.serializers import DoctorsCategorySerializer


class DoctorsCategoriesViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = DoctorsCategory.objects.all()
    serializer_class = DoctorsCategorySerializer
    # permission_classes =  [IsAUthenticatedOnly]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return DoctorsCategory.objects.all()[:2]
        return DoctorsCategory.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    def category(self, request):
        cats = DoctorsCategory.objects.all()
        return Response({'cats': [c.name for c in cats]})

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


# class DoctorsCategoriesListAPIView(APIView):
#     def get(self, request, pk):
#         categories = DoctorsCategory.objects.all().values()
#         return Response({'categories': DoctorsCategorySerializer(categories, many=True).data})
#
#     def post(self, request):
#         serializer = DoctorsCategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'category':serializer.data})
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
