from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list),
    path('customer/', views.customer_list, name = 'customer_list'),
    path('customer/<int:id>', views.customer_detail, name = 'customer_detail'),
    path('customer/new', views.customer_create, name = 'customer_create'),
    path('customer/<int:id>/edit', views.customer_update, name = 'customer_update'),
    path('customer/<int:id>/delete', views.customer_delete, name = 'customer_delete'),
    # path('students/', views.student_list, name = 'student_list'),
    # path('students/<int:id>', views.student_detail, name = 'student_detail'),
    # path('students/new', views.student_create, name = 'student_create'),
    # path('students/<int:id>/edit', views.student_update, name = 'student_edit'),
    # path('students/<int:id>/delete', views.student_delete, name = 'student_delete'),
]
