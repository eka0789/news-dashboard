from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # ===== PUBLIC LANDING PAGE =====
    path('', include('apps.news.public_urls')),    # halaman publik default

    # ===== CUSTOM DASHBOARD ADMIN =====
    path('dashboard/', include('apps.dashboard.urls')),  # dashboard admin
    path('dashboard/news/', include('apps.news.urls')),  # CRUD news/category
    path('dashboard/users/', include('apps.users.urls')), # CRUD user

    # ===== AUTH SYSTEM =====
    path('auth/', include('apps.users.auth_urls')),   # login/logout

    # ===== DJANGO ADMIN =====
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
