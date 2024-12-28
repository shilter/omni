from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include


urlpatterns = [
    path('', include('movie.views.home.urls')),
    path('admin/', admin.site.urls),
    path('home/',include('movie.views.home.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
