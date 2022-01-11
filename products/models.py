# from django.db import models
# from user.models import User
# # Create your models here.
#
#
# class Seller(models.Model):
#     seller_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_seller_name')
#     business_name = models.CharField(max_length=200, blank=False, null=False)
#     about_business = models.TextField(max_length=500, blank=False)
#     date_of_joining = models.DateField(auto_now_add=True)
#     active_status = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.seller_name
#
#
# def product_images(instance, filename):
#     return "product/images/{}/{}".format(instance.title, filename)
#
#
# class Products(models.Model):
#     seller = models.ForeignKey(User, related_name="user_product", on_delete=models.CASCADE)
#     title = models.CharField(max_length=100, blank=False, null=False)
#     price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
#     image = models.ImageField(upload_to=product_images, blank=True)
#     description = models.TextField(null=True, blank=True)
#     quantity = models.IntegerField(default=1)
#     is_deleted = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.title
#
#
#
