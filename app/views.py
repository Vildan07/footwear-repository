from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from .models import *


# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = 'app/index.html'
    context_object_name = 'shoes'
    extra_context = {
        'title': 'Products',
        'categories': Category.objects.filter(parent=None).order_by('name'),
    }


def product_by_category(request, gender):
    shoes = Product.objects.filter(category__gender=gender)
    categories = Category.objects.filter(parent=None)
    context = {
        'shoes': shoes,
        'categories': categories,
    }
    return render(request, 'app/man.html', context)


def product_detail(request, slug):
    product = Product.objects.filter(slug=slug)
    # category = Category.objects.all()
    context = {
        'product': product,
        # 'category': category,
    }
    return render(request, 'app/detail.html', context=context)


def product_category_man(request, slug):
    products = Product.objects.all()
    categories = Category.objects.filter(slug=slug)
    subcategories = Category.objects.filter(parent=not None)
    context = {
        'categories': categories,
        'products': products,
        'title': 'Man shoes',
        'page_name': 'Man',
        'subcategories': subcategories,
    }
    return render(request, 'app/man.html', context=context)


def product_category_woman(request, slug):
    products = Product.objects.all()
    categories = Category.objects.filter(slug=slug)
    subcategories = Category.objects.filter(parent=not None)
    context = {
        'categories': categories,
        'products': products,
        'title': 'Woman shoes',
        'page_name': 'Woman',
        'subcategories': subcategories,
    }
    return render(request, 'app/woman.html', context=context)


def about(request):
    return render(request, 'app/about.html')


def contact(request):
    return render(request, 'app/contact.html')


def cart(request):
    return render(request, 'app/cart.html')