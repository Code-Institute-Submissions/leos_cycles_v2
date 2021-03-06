from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('reviews/', include('reviews.urls')),
    path('services/', include('services.urls')),
    path('bike/', include('bike.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('userprofile/', include('userprofile.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
