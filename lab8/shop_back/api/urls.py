from django.urls import path
from api.views import product_list, get_product, categories_list, get_categories, products_list_by_categories

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('categories/', categories_list, name='categories-list'),
    path('products/<int:id>/', get_product, name='product-detail'),
    path('categories/<int:id>/', get_categories, name='categories-detail'),
    path('categories/<int:id>/products/', products_list_by_categories, name='product-list-by-categories'),

]