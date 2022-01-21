
from .models import Products, Category, SubCategory, Collections
from .serializers import ProductsSerializer, CategorySerializer, SubCategorySerializer, CollectionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# from .serializers import UserSerializer
# Create your views here.


class CollectionsView(APIView):
    """list top deal products"""

    def get(self, request, pk=None):
        if pk:
            collection = Collections.objects.get(pk=pk)
            print(list(collection))
            if not collection:
                return Response({"status": "category not found"},
                                status=status.HTTP_404_NOT_FOUND)
            serializer = CollectionSerializer(collection)
            return Response(serializer.data, status=status.HTTP_200_OK)
        collect_serializer = CollectionSerializer(Collections.objects.all(), many=True)
        return Response(collect_serializer.data, status=status.HTTP_200_OK)


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
        top_deal = Products.objects.filter().order_by("?")[0:20]

        cat_serializer = CategorySerializer(Category.objects.all().order_by('id'), many=True)
        product_serializer = ProductsSerializer(top_deal, many=True)
        context = {'products': product_serializer.data,
                   'categories': cat_serializer.data
                   }

        return Response(context, status=status.HTTP_200_OK)


class SubCategoryView(APIView):
    """ Sub categories view """

    def get(self, request, pk=None):
        if pk:
            products = Products.objects.filter(sub_category_id=pk)

            if not products:
                return Response({"status": "product not available"},
                                status=status.HTTP_404_NOT_FOUND)
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        top_deal = Products.objects.filter().order_by("?")[0:10]
        product_serializer = ProductsSerializer(top_deal, many=True)

        cat_serializer = SubCategorySerializer(SubCategory.objects.all().order_by('id'), many=True)
        context = {'products': product_serializer.data,
                   'categories': cat_serializer.data
                   }
        return Response(context, status=status.HTTP_200_OK)

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
