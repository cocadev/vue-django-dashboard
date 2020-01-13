from django.db import models
from conduit.apps.core.models import TimestampedModel


class Country(TimestampedModel):
    name = models.CharField(max_length=50, null=False, blank=False)
    phoneCode = models.CharField(max_length=5, null=False, blank=False )
    alpha2code = models.CharField(max_length=5, null=False, blank=False)
    alpha3code = models.CharField(max_length=5, null=False, blank=False )
    flag = models.FileField(upload_to='static/images/%Y/%m/%d/', null=True, blank=True)
    # slug = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return self.name


class Currency(TimestampedModel):
    symbol = models.CharField(max_length=10, null=False, blank=False, default=None)
    name = models.CharField(max_length=50, null=False, blank=False, default=None)
    symbol_native = models.CharField(max_length=20, null=False, blank=False, default=None)
    decimal_digits = models.IntegerField(default=0)
    rounding = models.FloatField(default=None)
    code = models.CharField(max_length=3, null=False, blank=False, default=None)
    name_plural = models.CharField(max_length=50, null=False, blank=False, default=None)

    def __str__(self):
        return "%s (%s)" % (self.code, self.symbol_native)


class Color(TimestampedModel):
    name = models.CharField(max_length=20, unique=True)
    value = models.CharField(max_length=10)

    def __str__(self):
        return "(%s)" % self.name


# class Currency(TimestampedModel):
#     name = models.CharField(max_length=20, db_index=True, unique=True)
#     code = models.CharField(max_length=20)
#     country = models.ForeignKey(
#         'eugene.Country', related_name='currencies', on_delete=models.CASCADE
#     )
#
#     def __str__(self):
#         return "%s (%s)" % (self.name, self.code)

