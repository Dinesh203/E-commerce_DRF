
from .models import User, Products, Category, SubCategory, Brand, Seller, CollectionOfCategories
from rest_framework import serializers
from django_countries.serializer_fields import CountryField


class ProductsSerializer(serializers.ModelSerializer):
    """ Product serializer """

    class Meta:
        """ product serializer Meta class """
        model = Products
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """ Category serializer """

    class Meta:
        """ Category serializer Meta class """
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    """ SubCategory serializer """

    class Meta:
        """ SubCategory serializer Meta class """
        model = SubCategory
        fields = '__all__'
