from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class HomePageView(LoginRequiredMixin, View):
    login_url = 'authentication'

    def get(self, request):
        return render(request, 'home_page/home_page.html')
# Create your views here.
# from rest_framework import permissions
#
#
# class IsAdminOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:  # запросы только для чтения данных
#             return True
#         return bool(request.user and request.user.is_staff)
#
#
# class IsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.user == request.user
#
#
# class WomenAPIListPagination(PageNumberPagination):
#     page_size = 3
#     page_size_query_param = 'page_size'
#     max_page_size = 2
#
#
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     pagination_class = WomenAPIListPagination
#
#
# class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#     permission_classes = (IsAuthenticated,)
#
#
# # authentication_classes = (TokenAuthentication,)
#
#
# class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#     permission_classes = (IsAdminOrReadOnly,)
#
#
# class WomenSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = Women
#         fields = "__all__"
#
#
# #
# # class MyCustomRouter(routers.SimpleRouter):
# #     routes = [  # список из наших маршрутов
# #         routers.Route(  #каждый класс опред один маршрут этот читает список статей
# #             url=r'^{prefix}$',
# #             mapping={
# #                 'get': 'list', #связывает тип запрооса с методом ViewSet
# #             },
# #             name='{basename}-list', #название маршрута
# #             detail=False, #список или отдельная запись
# #             initkwargs={'suffix': 'List'} # доп аргументы для коллекции кейворгс для
# #             # конкретного определения при срабатывании маршрута
# #         ),
# #
# #         routers.Route(  #читает одну статью по идентификатору
# #             url=r'^{prefix}/{lookup}$',
# #             mapping={
# #                 'get': 'retrieve',
# #             },
# #             name='{basename}-detail',
# #             detail=True,
# #             initkwargs={'suffix': 'Detail'}
# #         ),
# #         ]
# #
# #
# # router = MyCustomRouter()
# # router.register(r'women', WomenViewSet, basename='women')
# # print(router.urls)
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/drf-auth/', include('rest_framework.urls')),
#     # path('api/v1/', include(router.urls)),  #http://127.0.0.1:8000/api/v1/women/
#     # path('api/v1/womenlist/', WomenViewSet.as_view({'get':'list'})),
#     path('api/v1/women/', WomenAPIList.as_view()),
#     # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put':'update'})),
#     path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
#     # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view())
#     path('api/v1/womendestroy/<int:pk>/', WomenAPIDestroy.as_view()),
#     # path('api/v1/WomenViewSetwomendetail/<int:pk>/', WomenAPIDetailView.as_view())
#     path('api/v1/auth/', include('djoser.urls')),
#     re_path(r'^auth/', include('djoser.urls.authtoken')),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
# ]
