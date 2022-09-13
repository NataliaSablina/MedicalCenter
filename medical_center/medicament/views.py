from rest_framework import status, generics
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from medicament.models import (
    MedicamentCategory,
    Medicament,
    MedicamentSellerRelations,
    CommentMedicament,
)
from medicament.permissions import (
    IsAdminAndSellerOrReadOnly,
    IsOwnerSellerOrAdminOrReadOnly,
)
from medicament.serializers import (
    MedicamentCategorySerializer,
    MedicamentSerializer,
    OnlyMedicamentSerializer,
    MedicamentCommentSerializer,
    MedicamentSellerRelationsSerializer,
)
from user.permissions import IsOwnerOrAdminOrReadOnly


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


class CreateMedicamentAPIView(generics.CreateAPIView):
    queryset = Medicament.objects.all()
    serializer_class = OnlyMedicamentSerializer
    permission_classes = [IsAdminAndSellerOrReadOnly]


class UpdateMedicamentAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OnlyMedicamentSerializer
    permission_classes = [IsAdminAndSellerOrReadOnly]
    lookup_field = "title"

    def get_queryset(self):
        title = self.kwargs.get("title")
        if not title:
            return NotFound
        return Medicament.objects.get(title=title)


class CreateMedicamentCommentAPIView(generics.CreateAPIView):
    queryset = CommentMedicament.objects.all()
    serializer_class = MedicamentCommentSerializer


class UpdateDeleteMedicamentCommentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentMedicament.objects.all()
    serializer_class = MedicamentCommentSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        title = self.kwargs.get("title")
        if not title:
            return NotFound
        return CommentMedicament.objects.filter(title=title).first()


class CurrentMedicamentCommentsAPIListView(generics.ListAPIView):
    serializer_class = MedicamentCommentSerializer

    def get_queryset(self):
        title = self.kwargs.get("title")
        if not title:
            return NotFound
        return CommentMedicament.objects.filter(medicament__title=title)


class CreateMedicamentSellerRelationsAPIView(generics.CreateAPIView):
    queryset = MedicamentSellerRelations.objects.all()
    serializer_class = MedicamentSellerRelationsSerializer
    permission_classes = [IsAdminAndSellerOrReadOnly]


class UpdateDeleteMedicamentSellerRelationsAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = MedicamentSellerRelations.objects.all()
    serializer_class = MedicamentSellerRelationsSerializer
    permission_classes = [IsOwnerSellerOrAdminOrReadOnly]

    def get_object(self):
        title = self.kwargs.get("title")
        if not title:
            return NotFound
        return MedicamentSellerRelations.objects.filter(title=title).first()
