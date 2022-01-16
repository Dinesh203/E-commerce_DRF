from django.shortcuts import render
from .models import Products, ProductCategory
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
# from .serializers import UserSerializer
# Create your views here.


class ProductDetail(APIView):
    """product detail"""
    def get(self, request, pk=None):
        if pk:
            user = Products.objects.filter(pk=pk)
            if not user:
                return Response({"status": "invalid user or id"})
            serializer = UserSerializer(User.objects.get(pk=pk))
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if pk:
            try:
                serializer_data = UserSerializer(User.objects.get(id=pk), data=request.data, partial=True)
            except Exception as e:
                return HttpResponse(e)
            print(serializer_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return Response({"status": "success", "data": serializer_data.data})
            else:
                return Response({"status": "error", "data": serializer_data.errors})
        else:
            return Response({"status": "invalid detail or attribute"})

    def delete(self, request, pk=None):
        if pk:
            user = User.objects.filter(pk=pk)
            if not user:
                return Response({'status': 'page not found'})
            user.delete()
            return Response({"status": "success", "data": "Item Deleted"})
        else:
            return Response({'error': 'user id not found'})