from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


PRODUCT_CATEGORY = (
    ("", ""),
)

GENDER_CHOICE = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('other', 'OTHER')
)


class Address(models.Model):
    """User's Address detail table"""
    house_building_number = models.PositiveIntegerField(blank=True, null=True,
                                                        validators=[MaxValueValidator(99999)])
    village_city = models.CharField(max_length=50, blank=True)
    pin_code = models.PositiveIntegerField(blank=True, null=True,
                                           validators=[MaxValueValidator(999999),
                                                       MinValueValidator(1)])
    address = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.address


def user_profile(instance, filename):
    """  create media file folder with name create"""
    print("filename: ", filename)
    return "user_profile/{}/{}".format(instance.name, filename)


class User(AbstractUser):
    """Admin/User table
    """
    username = None
    # override username and email(unique)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=200, unique=True)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICE, blank=True)
    attachment_date = models.DateField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(9999999)]
                                          , blank=True,
                                          null=True)
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    profile_picture = models.ImageField(upload_to=user_profile, blank=True, null=True,
                                        default="media/user_profile/default_image" )

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
