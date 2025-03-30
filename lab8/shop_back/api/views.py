from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category

# Create your views here.

def product_list(request):
    products = [product.to_json() for product in Product.objects.all()]
    data = {'products': products}
    return JsonResponse(data, status=200)

def get_product(request, id):
    try:
        product = Product.objects.get(id=id)
        return JsonResponse(product.to_json(), status=200)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

def categories_list(request):
    categories = [category.to_json() for category in Category.objects.all()]
    data = {'categories': categories}
    return JsonResponse(data, status=200)

def get_categories(request, id):
    try:
        category = Category.objects.get(id=id)
        return JsonResponse(category.to_json(), status=200)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

def products_list_by_categories(request, id):
    products = Product.objects.filter(category=id)
    data = {'products': products}
    return JsonResponse(data, status=200)