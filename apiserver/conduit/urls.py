from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('conduit.apps.articles.urls')),
    path('api/', include('conduit.apps.authentication.urls')),
    path('api/', include('conduit.apps.profiles.urls')),
    path('api/', include('conduit.apps.eugene.urls')),

]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
