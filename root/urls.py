from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('apps.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = i18n_patterns(
#     path('admin/', admin.site.urls),
#     path('', include('apps.urls')),
#
#     path("__debug__/", include("debug_toolbar.urls"))
# ) + [path("ckeditor5/",
#            include('django_ckeditor_5.urls'),
#            name="ck_editor_5_upload_file"),