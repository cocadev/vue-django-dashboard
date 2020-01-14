from rest_framework import viewsets
from .serializers import *
from .forms import ProductPriceForm
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @api_view(['GET', 'POST'])
    def product_prices(request, id):
        if request.method == "GET":
            prices = ProductPrice.objects.filter(product_id=id).all()
            serializer = ProductPriceSerializer(prices, many=True)
            return Response({
                "results": serializer.data,
            })
        if request.method == "POST":
            form = ProductPriceForm(request.data)
            product = get_object_or_404(Product, pk=id, is_active=True)
            if form.is_valid():
                price = form.save(commit=False)
                price.product = product
                price.save()
                return Response({
                    "results": form.data,
                })
            else:
                return Response({
                    "err": form.errors
                }, status=400)

    @api_view(['GET', 'DELETE'])
    def product_price_profile(request, id, price_id):
        price = get_object_or_404(ProductPrice, pk=price_id, product=id)
        if request.method == "GET":
            serializer = ProductPriceSerializer(price)
            return Response({
                "results": serializer.data,
            })
        if request.method == "DELETE":
            price.delete()
            return Response({
                "results": "Deleted",
            })
