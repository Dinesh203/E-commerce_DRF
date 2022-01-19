from django.contrib import admin
from .models import User, Address
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    """User admin panel display fields"""
    list_display = ['id', 'email', 'name', 'profile_picture']


admin.site.register(User, UserAdmin)
admin.site.register(Address)
