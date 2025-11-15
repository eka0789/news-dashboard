from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('', views.user_list, name='users.index'),
    path('create/', views.user_create, name='users.create'),
    path('<int:id>/edit/', views.user_edit, name='users.edit'),
    path('<int:id>/delete/', views.user_delete, name='users.delete'),
]
