from django.contrib import admin
from django.urls import path,include

# For Media Files
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v3/app/",include("event.urls")),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)