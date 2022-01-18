
from .models import User, Products, Category, SubCategory, Seller, CollectionOfCategories
from rest_framework import serializers
from django_countries.serializer_fields import CountryField


class ProductsSerializer(serializers.ModelSerializer):
    """ Product serializer """
    seller = serializers.StringRelatedField(read_only=True)

    class Meta:
        """ product serializer Meta class """
        model = Products
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """ Category serializer """
    sub_category = serializers.StringRelatedField()

    class Meta:
        """ Category serializer Meta class """
        model = Category
        fields = ['id', 'name', 'icon', 'created']


class SubCategorySerializer(serializers.ModelSerializer):
    """ SubCategory serializer """

    class Meta:
        """ SubCategory serializer Meta class """
        model = SubCategory
        fields = '__all__'
