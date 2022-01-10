
from user.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    """ UserSerializer model class """

    class Meta:
        """ User serializer Meta class """
        model = User
        fields = ['name', 'email', 'password', 'gender', 'contact', 'date_of_birth', 'house_building_number',
                  'village_city', 'pin_code', 'address', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Create and return a new `User` instance, given the validated data."""
        user = super(UserSerializer, self).create(validated_data)
        user.password = make_password(validated_data['password'])
        user.save()
        print(user)
        return user
