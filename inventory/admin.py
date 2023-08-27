from django.contrib import admin
from inventory.models import Brand, Category,Product, Stock

admin.site.register(Brand)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Stock)
