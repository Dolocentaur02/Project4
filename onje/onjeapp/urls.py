from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', views.Product_list),
    path('product/', views.Product_list, name='product_list'),
    path('product/<int:id>', views.Product_detail, name='product_detail'),
    path('product/new', views.Product_create, name='product_create'),
    path('product/<int:id>/edit', views.Product_update, name='product_update'),
    path('product/<int:id>/delete', views.Product_delete, name='product_delete'),
    path('contact/', views.contact_list, name='contact_list'),
    path('contact/<int:id>', views.contact_detail, name='contact_detail'),
    path('contact/new', views.contact_create, name='contact_create'),
    path('contact/<int:id>/edit', views.contact_update, name='contact_edit'),
    path('contact/<int:id>/delete', views.contact_delete, name='contact_delete'),
    path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
    path('search/', views.searchproducts, name='search'),

]
