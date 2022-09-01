from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from medicament.models import MedicamentCategory, Medicament, MedicamentSellerRelations
from medicament.serializers import (
    MedicamentCategorySerializer,
    MedicamentCategoryModelSerializer,
    MedicamentSerializer,
    OnlyMedicamentSerializer,
)


class MedicamentCategoryListView(APIView):
    def get(self, request):
        categories = MedicamentCategory.objects.all().values("id", "title")
        # return Response({'categories': MedicamentCategorySerializer(categories, many=True).data})
        return Response(MedicamentCategorySerializer(categories, many=True).data)


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
        title = kwargs.get("title", None)
        if not title:
            Response({"Metod PUT not allowed"})
        try:
            instance = MedicamentCategory.objects.get(title=title)
        except:
            return Response({"error: object doesn't exists"})
        serializer = MedicamentCategorySerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, result, *args, **kwargs):
        title = kwargs.get("title", None)
        if not title:
            Response({"Metod DELETE not allowed"})
        try:
            instance = MedicamentCategory.objects.get(title=title)
        except:
            return Response({"error: object doesn't exists"})
        instance.delete()
        return Response(
            data={"dlete": f"{title} was deleted"}, status=status.HTTP_200_OK
        )


class CurrentCategoryMedicamentListAPIView(generics.ListAPIView):
    serializer_class = MedicamentSerializer

    def get_queryset(self):
        title = self.kwargs.get("title")
        return MedicamentSellerRelations.objects.filter(
            medicament__category__title=title
        )


class CurrentMedicamentListAPIView(generics.ListAPIView):
    serializer_class = MedicamentSerializer

    def get_queryset(self):
        title = self.kwargs.get("title")
        return MedicamentSellerRelations.objects.filter(medicament__title=title)


class MedicamentListAPIView(generics.ListAPIView):
    queryset = Medicament.objects.all()
    serializer_class = OnlyMedicamentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_fields = ['title']
    # searchset_fields = ['title', 'brief_instruction', 'instruction']
