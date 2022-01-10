
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


def user_profile(instance, filename):
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
    contact = models.CharField(max_length=12)
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    house_building_number = models.IntegerField(blank=True, null=True,
                                                validators=[MinValueValidator(1), MaxValueValidator(6)])
    village_city = models.CharField(max_length=50, blank=True)
    pin_code = models.PositiveIntegerField(default=000000, validators=[MaxValueValidator(6)])
    address = models.CharField(max_length=15, blank=False, null=False)
    profile_picture = models.ImageField(upload_to=user_profile, blank=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
