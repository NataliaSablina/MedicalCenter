from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from medicament.models import MedicamentCategory, Medicament
from medicament.serializers import MedicamentCategorySerializer, MedicamentCategoryModelSerializer, \
    MedicamentModelSerializer


class MedicamentCategoryListView(APIView):
    def get(self, request):
        categories = MedicamentCategory.objects.all().values('id', 'title')
        return Response({'categories': MedicamentCategorySerializer(categories, many=True).data})


class MedicamentCategoryView(APIView):
    permission_classes = [IsAdminUser]
    # {
    #     "id": 1,
    #     "title": "sdr"
    # }

    def post(self, request):
        serializer = MedicamentCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            Response({"Metod PUT not allowed"})
        try:
            instance = MedicamentCategory.objects.get(pk=pk)
        except:
            return Response({"error: object doesn't exists"})
        serializer = MedicamentCategorySerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, result, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            Response({"Metod DELETE not allowed"})
        try:
            instance = MedicamentCategory.objects.get(pk=pk)
        except:
            return Response({"error: object doesn't exists"})
        instance.delete()
        return Response(data={'dlete':f'{pk} was deleted'}, status=status.HTTP_200_OK)


class CurrentCategoryMedicamentListAPIView(generics.ListAPIView):
    serializer_class = MedicamentModelSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Medicament.objects.filter(category__id=pk)

