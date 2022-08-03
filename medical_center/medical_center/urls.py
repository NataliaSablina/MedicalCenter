from django.contrib import admin
from django.urls import path, include
from home_page.views import HomePageView
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
