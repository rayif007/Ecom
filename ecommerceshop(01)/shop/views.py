from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Product


# Create your views here.
# venv- ecommerceshop

def allproducts(request, slug_c=None):
    page_c = None
    products = None
    if slug_c != None:
        page_c = get_object_or_404(Category, slug=slug_c)
        products = Product.objects.all().filter(category=page_c, available=True)
    else:
        products = Product.objects.all().filter(available=True)

    return render(request, 'home.html', {'category': page_c, 'products': products})


def prod_det(request, slug_c, slug_p):
    try:
        products = Product.objects.get(category__slug=slug_c, slug=slug_p)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': products})
