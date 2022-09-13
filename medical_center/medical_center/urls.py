from django.contrib import admin
from django.urls import path, include

from user.views import HomePageView
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home_page/", HomePageView.as_view(), name="home_page"),
    path("user/", include("user.urls")),
    path("doctors/", include("doctors.urls")),
    path("seller/", include("seller.urls")),
    path("timetable/", include("timetable.urls")),
    path("medicament/", include("medicament.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
