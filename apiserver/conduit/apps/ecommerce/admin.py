from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Address)
admin.site.register(Employee)
admin.site.register(Invoice)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ProductPrice)

