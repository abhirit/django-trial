from django.urls import path

from . import views

urlpatterns = [
    path('calculate',views.home, name='calculate'),
    path('add', views.add, name='add')

]
