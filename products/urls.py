from django.urls import path
from . import views

urlpatterns = [
    path('<product_id>', views.product_detail, name='product_detail'),
    path('', views.all_products, name='products'),
]
