from django.db import models
from conduit.apps.core.models import TimestampedModel


class Country(TimestampedModel):
    country = models.CharField(max_length=50)
    slug = models.SlugField(db_index=True, unique=True)
    code = models.IntegerField()
    flag = models.FileField(upload_to='static/images/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.country


class Currency(TimestampedModel):
    name = models.CharField(max_length=20, db_index=True, unique=True)
    code = models.CharField(max_length=20)
    country = models.ForeignKey(
        'eugene.Country', related_name='currencies', on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s (%s)" % (self.name, self.code)


