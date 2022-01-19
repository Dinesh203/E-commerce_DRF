from .views import *
from django.urls import path


urlpatterns = [
    path('product_detail/', ProductDetail.as_view(), name='products_detail'),
    path('product_detail/<int:pk>', ProductDetail.as_view(), name='products_detail'),
    path('category/', CategoryView.as_view(), name='category_view'),
    path('category/<int:pk>', CategoryView.as_view(), name='category_view_by_id'),
    path('subcategory/', SubCategoryView.as_view(), name='subcategory_view'),
    path('subcategory/<int:pk>', SubCategoryView.as_view(), name='subcategory_view_by_id')

]
