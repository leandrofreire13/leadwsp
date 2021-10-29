from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('referidos', views.list_referidos, name='referidos'),
    path('referidos/new', views.referido_new, name="referido_new")
]