from django.db import models
from user.models import User
# Create your models here.


class Seller(models.Model):
    seller_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_seller_name')
    business_name = models.CharField(max_length=200, blank=False, null=False)
    about_business = models.TextField(max_length=500, blank=False)
    date_of_joining = models.DateField(auto_now_add=True)
    active_status = models.BooleanField(default=False)

    def __str__(self):
        return self.seller_name


def product_images(instance, filename):
    return "product/images/{}/{}".format(instance.title, filename)


class Products(models.Model):
    """ Products details """
    title = models.CharField(max_length=100, blank=False, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    image = models.ImageField(upload_to=product_images, blank=True, null=True)
    seller = models.ForeignKey(User, related_name="user_product", on_delete=models.CASCADE,
                               null=True, blank=True)
    feature = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    """ Product sub category """
    sub_category_name = models.CharField(max_length=100, blank=False, default="")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.sub_category_name


class Brand(models.Model):
    """ Product categories by brands """
    brand_name = models.CharField(max_length=100, blank=False, default="")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.brand_name


def category_image(instance, filename):
    return "category/icons/{}/{}".format(instance.name, filename)


class Category(models.Model):
    """ Product sub category"""
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='category_image/', blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CollectionOfCategories(models.Model):
    """collection of categories """
    collection_name = models.CharField(max_length=100, blank=False, default="")
    categories_name = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.collection_name

