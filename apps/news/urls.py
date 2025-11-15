from django.urls import path
from . import views

urlpatterns = [
 
     # CATEGORY CRUD
    path('category/', views.category_list, name='category.index'),
    path('category/create/', views.category_create, name='category.create'),
    path('category/<int:id>/edit/', views.category_edit, name='category.edit'),
    path('category/<int:id>/delete/', views.category_delete, name='category.delete'),
    path('', views.news_list, name='news.index'),
    path('create/', views.news_create, name='news.create'),
    path('<int:id>/edit/', views.news_edit, name='news.edit'),
    path('<int:id>/delete/', views.news_delete, name='news.delete'),
]
