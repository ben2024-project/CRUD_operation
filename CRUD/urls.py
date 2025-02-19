"""
URL configuration for CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from myapp import views


urlpatterns = [
    
    path('admin/', admin.site.urls),

    path("category/add/",views.CategoryCreate.as_view(),name="cat-add"),

    path("product/add/",views.ProductCreate.as_view(),name="product-add"),

    path("product/all/",views.ProductList.as_view(),name="product-list"),

    path("product/<int:pk>/",views.ProductDetail.as_view(),name="product-detail"),

    path("product/<int:pk>/delete/",views.ProductDelete.as_view(),name="product-delete"),

    path("product/<int:pk>/edit/",views.ProductUpdate.as_view(),name="product-edit"),

    path("product/<int:pk>/category/",views.CategoryFilter.as_view(),name="cat-filter"),
]

