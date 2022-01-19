from django.contrib import admin
from .models import Products, Category, SubCategory, Seller, CollectionOfCategories, Feature, AvailableOffer
# Register your models here

admin.site.register(CollectionOfCategories)
admin.site.register(SubCategory)
admin.site.register(Seller)
admin.site.register(Feature)
admin.site.register(AvailableOffer)


class CategoryAdmin(admin.ModelAdmin):
    """ product categories interface configure"""
    list_display = ['id', 'name', 'icon', 'sub_category']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    """ product admin interface configure"""
    list_display = ['id', 'title', 'price']


admin.site.register(Products, ProductAdmin)

