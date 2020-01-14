from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('products/<int:id>/prices', ProductViewSet.product_prices),
    path('products/<int:id>/prices/<int:price_id>', ProductViewSet.product_price_profile),
]

