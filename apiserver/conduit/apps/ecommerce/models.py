from django.db import models
from .utils import Taxes, MAP, AddressMetaData
from django.core.validators import RegexValidator


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', blank=True)
    position = models.CharField(max_length=50, verbose_name='Position', blank=True)
    tax = models.IntegerField(default=0, verbose_name='Tax', choices=Taxes.choices)
    is_active = models.BooleanField(default=True)
    description = models.TextField(verbose_name='Description', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Client(models.Model):
    email = models.EmailField(verbose_name='Email Address', max_length=255, unique=True,)
    first_name = models.CharField(max_length=255, verbose_name='First name', blank=True)
    last_name = models.CharField(max_length=255, verbose_name='Last name', blank=True)
    company_name = models.CharField(max_length=255, verbose_name='Company name', blank=True)

    phone_number = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                                               message="Phone number must be entered in the format: "
                                                                       "'+491725784200'. Up to 15 digits allowed.")],
                                    max_length=17, verbose_name='Phone number', blank=True)
    fax_number = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                                             message="Phone number must be entered in the format: "
                                                                     "'+491725784200'. Up to 15 digits allowed.")],
                                  max_length=17, verbose_name='Fax number', blank=True)
    tax_number = models.CharField(max_length=255, verbose_name='Tax number', blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Creation date', blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


class Address(models.Model):
    client = models.ForeignKey(to=Client, related_name="addresses", null=True, blank=True, on_delete=models.CASCADE)
    business_address_street = models.CharField(max_length=254, verbose_name='Street', blank=True)
    business_address_house_number = models.CharField(max_length=5, verbose_name='House number', blank=True)
    business_address_zipecode = models.CharField(max_length=5, verbose_name='Zip code', blank=True)
    business_address_city = models.CharField(max_length=5, verbose_name='City', choices=MAP.cities, blank=True)
    business_address_country = models.CharField(max_length=3, verbose_name='Country', choices=MAP.countries, default="DE", blank=True)
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                                               message="Phone number must be entered in the format: "
                                                                       "'+49172578420'. Up to 15 digits allowed.")],
                                    max_length=17, verbose_name='Phone number', blank=True)
    type = models.CharField(max_length=10, verbose_name='Type', choices=AddressMetaData.types, default='1', blank=False)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
