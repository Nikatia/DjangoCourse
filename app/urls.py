"""
URL configuration for suppliers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import landingview, productlistview, supplierlistview, \
                   addsupplier, addproduct, \
                   deleteproduct, confirmdeleteproduct, \
                   deletesupplier, confirmdeletesupplier, \
                   edit_product_get, edit_product_post, \
                   edit_supplier_get, edit_supplier_post, \
                   searchsuppliers, searchproducts, search_suppliers_products

urlpatterns = [
    path('', landingview),

    #Suppliers:
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post),
    path('search-suppliers/', searchsuppliers),


    #Products:
    path('products/', productlistview),   
    path('add-product/', addproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    path('search-products/', searchproducts),
    path('products-by-supplier/<int:id>/', search_suppliers_products)
]
