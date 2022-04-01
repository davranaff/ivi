from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page , name='home_page_url'),
    path('product_detail/<pk>', views.product_detail , name = 'product_detail_url'),
]