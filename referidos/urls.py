from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('roteiro', views.roteiro, name='roteiro'),
    path('referidos', views.list_referidos, name='referidos'),
    path('referidos/dados', views.lista_dados, name='dados'),
    path('referidos/new', views.referido_new, name="referido_new"),
    path('referidos/<int:pk>/edit', views.referido_edit, name="referido_edit"),
    path('upload', views.upload, name='upload'),
]