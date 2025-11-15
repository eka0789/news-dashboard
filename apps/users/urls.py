from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='users.index'),   # WAJIB ADA!!!
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]
