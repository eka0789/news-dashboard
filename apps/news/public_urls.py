from django.urls import path
from . import public_views

urlpatterns = [
    path('', public_views.landing_page, name='public.landing'),
    path('news/<slug:slug>/', public_views.public_detail, name='public.news.detail'),
    path('category/<slug:slug>/', public_views.public_category, name='public.news.category'),
]
