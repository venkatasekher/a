"""Project8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from App8 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view_all_products/',views.view_all_products),
    path('view_all_productsdj/',views.View_All_Products.as_view()),
    path('view_one_product/<one>',views.view_one_product),
    path('view_one_productdj/<one>',views.View_One_Product.as_view()),
    path('insert_one_product/',views.InsertOneProduct.as_view()),
    path('insert_multiple_products/',views.InsertMultipleProducts.as_view()),
    path('update_product/<product>',views.UpdateProduct.as_view()),
    path('delete_product/<product>',views.DeleteProduct.as_view()),

]
