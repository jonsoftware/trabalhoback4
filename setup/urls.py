"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cadfun.views import (
    FuncionarioListView, FuncionarioCreateView, FuncionarioUpdateView, FuncionarioDeleteView, FaltaListView, FaltaCreateView, FaltaUpdateView, FaltaDeleteView, FuncionarioDetailView
)

urlpatterns = [
        path("admin/", admin.site.urls),
    
    path("", FuncionarioListView.as_view(), name="funcionario_list"),
    path("funcionario/create/", FuncionarioCreateView.as_view(), name="funcionario_create"),
    path("funcionario/<int:pk>/update/", FuncionarioUpdateView.as_view(), name="funcionario_update"),
    path("funcionario/<int:pk>/delete/", FuncionarioDeleteView.as_view(), name="funcionario_delete"),
    
    path('funcionario/<int:pk>/', FuncionarioDetailView.as_view(), name='funcionario_detail'),
    
    path('faltas/', FaltaListView.as_view(), name='lista_faltas'),
    path('faltas/criar/', FaltaCreateView.as_view(), name='criar_falta'),
    path('faltas/editar/<int:pk>/', FaltaUpdateView.as_view(), name='editar_falta'),
    path('faltas/excluir/<int:pk>/', FaltaDeleteView.as_view(), name='excluir_falta'),
]