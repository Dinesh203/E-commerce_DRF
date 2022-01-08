from django.db import models
from django.db import models
from user.manager import CustomUserManager
import logging
# Create your models here.


PRODUCT_CATEGORY = (
    ("", ""),
)

GENDER_CHOICE = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('other', 'OTHER')
)


class User(CustomUserManager):
    """Admin/User table
    """
    username = None
    # override username and email(unique)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=200, unique=True)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICE, blank=True)
    attachment_date = models.DateField(auto_now_add=True)
    contact = models.CharField(max_length=12)
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    city = models.CharField(max_length=50, )
    district = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=15, default="", blank=True)

    profile_picture = models.ImageField(upload_to='profile/', blank=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
