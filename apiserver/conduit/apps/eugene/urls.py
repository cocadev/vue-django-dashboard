from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyViewSet, CountryViewSet
from django.conf.urls.static import static
from django.conf import settings

# from .views import (
#     get_countries, add_country, detail_country, update_country, delete_country
# )

router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet)
router.register(r'countries', CountryViewSet)

urlpatterns = [


    path('', include(router.urls)),

    # path('countries/', get_countries, name="secure.countries"),
    # path('countries/add/', add_country, name="secure.country.add"),
    # path('countries/<int:pk>/', detail_country, name="secure.country.detail"),
    # path('countries/<int:pk>/update/', update_country, name="secure.country.update"),
    # path('countries/<int:pk>/delete/', delete_country, name="secure.country.delete"),
]

