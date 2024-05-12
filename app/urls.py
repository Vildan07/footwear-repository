from django.urls import path
from django.views.generic import detail

from .views import *
urlpatterns = [
    path('', ProductList.as_view(), name='index'),
    path('detail/<slug:slug>/', product_detail, name='detail'),
    path('category_man/<slug:slug>/', product_category_man, name='man_category'),
    path('category_woman/<slug:slug>/', product_category_woman, name='woman_category'),

    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('categories/<str:gender>/', product_by_category, name='by_category'),
]