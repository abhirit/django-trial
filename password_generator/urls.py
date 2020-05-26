from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('password_generator', views.password, name = 'password'),
]