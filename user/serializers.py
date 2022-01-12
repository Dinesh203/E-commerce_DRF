
from user.models import User, Address
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django_countries.serializer_fields import CountryField


class UserSerializer(serializers.ModelSerializer):
    """ UserSerializer model class """

    class Meta:
        """ User serializer Meta class """
        model = User
        fields = ['id', 'name', 'email', 'password', 'gender', 'contact', 'date_of_birth']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Create and return a new `User` instance, given the validated data."""
        user = super(UserSerializer, self).create(validated_data)
        user.password = make_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """ Update user's instance"""
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class AddressSerializer(serializers.ModelSerializer):
    """ Address serializer model class"""

    class Meta:
        """ address serializer Meta class """
        model = Address
        fields = ['id', 'house_building_number', 'village_city', 'pin_code', 'address']
