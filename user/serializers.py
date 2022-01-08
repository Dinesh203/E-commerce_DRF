
from user.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class EmployeeSerializer(serializers.ModelSerializer):
    """ UserSerializer model class """

    class Meta:
        """ User serializer Meta class """
        model = User
        fields = ['name', 'email', 'password', 'gender', 'contact', 'date_of_birth', 'address']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Create and return a new `User` instance, given the validated data."""
        user = super(EmployeeSerializer, self).create(validated_data)
        user.password = make_password(validated_data['password'])
        user.save()
        return user
