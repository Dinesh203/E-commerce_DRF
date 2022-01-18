from django.db import models
from user.models import User

# Create your models here.

COLOR_CHOICES = (
    ('RED', 'red'),
    ('WHITE', 'white'),
    ('SKY_BLUE', 'sky_blue'),
    ('BLACK', 'black'),
    ('SILVER', 'SILVER'),
    ('GREEN', 'green')
)


class Seller(models.Model):
    """ seller detail table """
    seller_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_seller_name')
    business_name = models.CharField(max_length=200, blank=False, null=False)
    about_business = models.TextField(max_length=500, blank=False)
    date_of_joining = models.DateField(auto_now_add=True)
    active_status = models.BooleanField(default=False)

    def __str__(self):
        return self.seller_name.name


class Feature(models.Model):
    """ make product feature """
    product_name = models.CharField(max_length=100, null=True, blank=True)
    feature1 = models.CharField(max_length=200, null=True, blank=True)
    feature2 = models.CharField(max_length=200, null=True, blank=True)
    feature3 = models.CharField(max_length=200, null=True, blank=True)
    feature4 = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    specification = models.CharField(max_length=500, blank=True, null=True)
    color = models.CharField(choices=COLOR_CHOICES, max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.product_name


class AvailableOffer(models.Model):
    """ Available offer tabel"""
    product_name = models.CharField(max_length=100, blank=True, null=True)
    offer1 = models.CharField(max_length=100, blank=True, null=True)
    offer2 = models.CharField(max_length=100, blank=True, null=True)
    offer3 = models.CharField(max_length=100, blank=True, null=True)
    offer4 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.product_name


def product_images(instance, filename):
    """ make product image path"""
    return "media/product/images/{}/{}".format(instance.title, filename)


class Products(models.Model):
    """ Products details """
    title = models.CharField(max_length=100, blank=False, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    image = models.ImageField(upload_to=product_images, blank=True, null=True)
    seller = models.ForeignKey(User, related_name="user_product", on_delete=models.CASCADE,
                               null=True, blank=True)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, blank=True, null=True)
    available_offer = models.ForeignKey(AvailableOffer, on_delete=models.CASCADE,
                                        blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    """ Product sub category """
    sub_category_name = models.CharField(max_length=100, blank=False, default="")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.sub_category_name


def category_image(instance, filename):
    """ make category image path """
    return "category/icons/{}/{}".format(instance.name, filename)


class Category(models.Model):
    """ Product sub category"""
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='category_image/', blank=True, null=True)
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

# class Brand(models.Model):
#     """ Product categories by brands """
#     brand_name = models.CharField(max_length=100, blank=False, null=True)
#
#     def __str__(self):
#         return self.brand_name
