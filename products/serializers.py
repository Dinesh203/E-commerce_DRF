
from .models import User, Products
from rest_framework import serializers
from django_countries.serializer_fields import CountryField


class ProductsSerializer(serializers.ModelSerializer):
    """ Product serializer """

    class Meta:
        """ product serializer Meta class """
        model = Products
        fields = '__all__'

# class AddressSerializer(serializers.ModelSerializer):
#     """ Address serializer model class
#     """
#     class Meta:
#         """ address serializer Meta class """
#         model = Address
#         fields = ['id', 'house_building_number', 'village_city', 'pin_code', 'address']
