from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Product_list),
    path('product/', views.Product_list, name='product_list'),
    path('product/<int:id>', views.Product_detail, name='product_detail'),
    path('product/new', views.Product_create, name='Product_create'),
    path('product/<int:id>/edit', views.Product_update, name='Product_update'),
    path('product/<int:id>/delete', views.Product_delete, name='Product_delete'),
    path('contact/', views.contact_list, name='contact_list'),
    path('contact/<int:id>', views.contact_detail, name='contact_detail'),
    path('contact/new', views.contact_create, name='contact_create'),
    path('contact/<int:id>/edit', views.contact_update, name='contact_update'),
    path('contact/<int:id>/delete', views.contact_delete, name='contact_delete'),
    path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success')
    # path('students/', views.student_list, name = 'student_list'),
    # path('students/<int:id>', views.student_detail, name = 'student_detail'),
    # path('students/new', views.student_create, name = 'student_create'),
    # path('students/<int:id>/edit', views.student_update, name = 'student_edit'),
    # path('students/<int:id>/delete', views.student_delete, name = 'student_delete'),
]
