from .views import *
from django.urls import path

urlpatterns = [
    path('product_detail/', ProductDetail.as_view(), name='products_detail'),
    path('product_detail/<int:pk>', ProductDetail.as_view(), name='products_detail')

]
