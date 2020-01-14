from django.db import models
from .utils import *
from django.core.validators import RegexValidator


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', unique=True)
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


class Employee(models.Model):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=255, verbose_name='First name', blank=True)
    last_name = models.CharField(max_length=255, verbose_name='Last name', blank=True)
    avatar = models.CharField(max_length=255, verbose_name='Avatar', blank=True)
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                                               message="Phone number must be entered in the format: "
                                                                       "'+49172578420'. Up to 15 digits allowed.")],
                                    max_length=17, verbose_name='Phone number', blank=True)
    business_address_street = models.CharField(max_length=254, verbose_name='Street', blank=True)
    business_address_house_number = models.CharField(max_length=5, verbose_name='House number', blank=True)
    business_address_zipecode = models.CharField(max_length=5, verbose_name='Zip code', blank=True)
    business_address_city = models.CharField(max_length=5, verbose_name='City', choices=MAP.cities, blank=True)
    business_address_country = models.CharField(max_length=3, verbose_name='Country', choices=MAP.countries, blank=True)
    position = models.CharField(max_length=255, verbose_name='Position', blank=True)
    note = models.TextField(verbose_name='Note', blank=True)
    birthday = models.DateTimeField(verbose_name='Creation Date', null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Creation date', blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.email


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', blank=True)
    article_number = models.CharField(max_length=255, verbose_name='Article number', blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    short_description = models.TextField(max_length=120, verbose_name='Short description', blank=True)
    description = models.TextField(verbose_name='Note', blank=True)
    availability_start_date = models.DateTimeField(verbose_name='availability Start Date', null=True, blank=True)
    availability_end_date = models.DateTimeField(verbose_name='availability End Date', null=True, blank=True)

    def __str__(self):
        return self.name


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, related_name='prices', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    units = models.CharField(max_length=50, verbose_name='Units', choices=Units.choices, blank=True)
    description = models.TextField(verbose_name='Note', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation date', blank=True)

    def __str__(self):
        return "%s ( %s / %s )" % (self.product, self.price, self.units)


class Invoice(models.Model):
    uuid = models.CharField(max_length=255, verbose_name='Invoice Number')
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    client_archive_name = models.CharField(max_length=255, verbose_name='Client Archive Name', blank=True, null=True)
    client_archive_address = models.CharField(max_length=255, verbose_name='Client Archive Address', blank=True, null=True)
    client_archive_email = models.CharField(max_length=255, verbose_name='Client Archive Email', blank=True, null=True)
    client_archive_phone = models.CharField(max_length=255, verbose_name='Client Archive Phone', blank=True, null=True)
    client_archive_city = models.CharField(max_length=5, verbose_name='City', choices=MAP.cities, blank=True)
    client_archive_country = models.CharField(max_length=3, verbose_name='Country', choices=MAP.countries, blank=True)
    created_date = models.DateTimeField(auto_now=True, verbose_name='Creation date', blank=True)
    issue_date = models.DateTimeField(verbose_name='Issue Date', null=True, blank=True)
    delivery_date = models.DateTimeField(verbose_name='Delivery date', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    state = models.IntegerField(default=1, choices=InvoiceMetaData.states)

    def __str__(self):
        return self.uuid


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    product_archive_name = models.TextField(verbose_name='Product Archive Name', blank=True, null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, default=None, related_name='orders')
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    quantity = models.BigIntegerField(default=1)
    units = models.CharField(max_length=50, verbose_name='Units', choices=Units.choices, blank=True)
    tax = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, verbose_name='Tax', choices=Taxes.choices)
    description = models.TextField(verbose_name='Description', blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation date', blank=True)

    def __str__(self):
        return "order % of invoice %".format(self.pk, self.invoice.uuid)


