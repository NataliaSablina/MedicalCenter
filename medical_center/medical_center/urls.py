from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
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
