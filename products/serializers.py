
from .models import User, Products, Category, SubCategory, Collections, Cart
from rest_framework import serializers
from django_countries.serializer_fields import CountryField


class FeatureSerializer(serializers.ModelSerializer):
    """feature model serializer class"""
    class Meta:
        """ product serializer Meta class """
        model = Products
        fields = ['id', 'product_name', 'feature1', 'feature2', 'feature3', 'feature4', 'brand', 'specification',
                  'color', 'size']


class ProductsSerializer(serializers.ModelSerializer):
    """ Product serializer """
    seller = serializers.StringRelatedField(read_only=True)
    # feature = serializers.StringRelatedField()

    class Meta:
        """ product serializer Meta class """
        model = Products
        fields = ['id', 'title', 'image', 'seller', 'actual_price',
                  'discount_price', 'feature', 'available_offer', 'description']
        # depth = 1


class CategorySerializer(serializers.ModelSerializer):
    """ Category serializer """
    sub_category = serializers.StringRelatedField()

    class Meta:
        """ Category serializer Meta class """
        model = Category
        fields = ['id', 'name', 'icon', 'sub_category']


class SubCategorySerializer(serializers.ModelSerializer):
    """ SubCategory serializer """

    class Meta:
        """ SubCategory serializer Meta class """
        model = SubCategory
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    """ CollectionOfCategories serializer """
    photo_url = serializers.SerializerMethodField()

    class Meta:
        """ CollectionOfCategories serializer Meta class """
        model = Collections
        fields = ['id', 'collection_name', 'photo_url']

    def get_photo_url(self, car):
        request = self.context.get('request')
        collection = Collections.objects.all()
        for i in collection:
            print(i.image.url)
            # print(request.data)
            # print("path", request.build_absolute_uri('/')[:-1] + i.image.url)
        print('seri_img_path', request.build_absolute_uri)
        photo_url = request.build_absolute_uri('/')[:-1] + i.image.url
        print('seri_img_path', photo_url)
        return photo_url


class CartSerializer(serializers.ModelSerializer):
    """ cart serializer """
    # user = serializers.StringRelatedField()
    # products = serializers.StringRelatedField()

    class Meta:
        """ cart serializer Meta class """
        model = Cart
        fields = ['id', 'user', 'products', 'total_amount', 'quantity']

