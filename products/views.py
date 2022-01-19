
from .models import Products, Category, SubCategory, Seller
from .serializers import ProductsSerializer, CategorySerializer, SubCategorySerializer
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
            product = Products.objects.filter(pk=pk)
            if not product:
                return Response({"status": "invalid user or id"})
            serializer = ProductsSerializer(Products.objects.get(pk=pk))
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        product = Products.objects.all().order_by('id')
        serializer = ProductsSerializer(product, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class CategoryView(APIView):
    """ Category view """
    def get(self, request, pk=None):
        if pk:
            category = Category.objects.get(pk=pk)
            if not category:
                return Response({"status": "category not found"},
                                status=status.HTTP_404_NOT_FOUND)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        cat_serializer = CategorySerializer(Category.objects.all().order_by('id'), many=True)
        return Response(cat_serializer.data, status=status.HTTP_200_OK)


class SubCategoryView(APIView):
    """ Sub categories view """

    def get(self, request, pk=None):
        if pk:
            sub_category = SubCategory.objects.get(pk=pk)
            if not sub_category:
                return Response({"status": "category not found"},
                                status=status.HTTP_404_NOT_FOUND)
            serializer = SubCategorySerializer(sub_category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        cat_serializer = SubCategorySerializer(SubCategory.objects.all().order_by('id'), many=True)
        return Response(cat_serializer.data, status=status.HTTP_200_OK)


    # def post(self, request):
    #     print(request.data)
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def patch(self, request, pk=None):
    #     if pk:
    #         try:
    #             serializer_data = UserSerializer(User.objects.get(id=pk), data=request.data, partial=True)
    #         except Exception as e:
    #             return HttpResponse(e)
    #         print(serializer_data)
    #         if serializer_data.is_valid():
    #             serializer_data.save()
    #             return Response({"status": "success", "data": serializer_data.data})
    #         else:
    #             return Response({"status": "error", "data": serializer_data.errors})
    #     else:
    #         return Response({"status": "invalid detail or attribute"})
    #
    # def delete(self, request, pk=None):
    #     if pk:
    #         user = User.objects.filter(pk=pk)
    #         if not user:
    #             return Response({'status': 'page not found'})
    #         user.delete()
    #         return Response({"status": "success", "data": "Item Deleted"})
    #     else:
    #         return Response({'error': 'user id not found'})