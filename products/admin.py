from django.contrib import admin
from .models import Products, Category, SubCategory, Seller, CollectionOfCategories, Feature, AvailableOffer
# Register your models here

admin.site.register(CollectionOfCategories)
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Seller)
admin.site.register(Feature)
admin.site.register(AvailableOffer)
