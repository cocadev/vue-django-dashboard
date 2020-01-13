from rest_framework import serializers
from .models import Country, Currency, Color


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name', 'phoneCode', 'alpha2code', 'alpha3code')

    # def to_representation(self, obj):
    #     return obj.country


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ('id', 'symbol', 'name', 'symbol_native', 'decimal_digits', 'rounding', 'code', 'name_plural')


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ('id', 'name', 'value')


# class CurrencySerializer(serializers.ModelSerializer):
#     # country_name = serializers.ReadOnlyField(source='country.name')
#     # country = CountrySerializer()
#
#     class Meta:
#         model = Currency
#         # fields = "__all__"
#         fields = ('id', 'name', 'code', 'country')


