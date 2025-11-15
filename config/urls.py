from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # app routes
    path('', include('apps.dashboard.urls')),
    path('news/', include('apps.news.urls')),
    

    path('auth/', include('apps.users.auth_urls')),   # khusus login/logout
    path('users/', include('apps.users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
