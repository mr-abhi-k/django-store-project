from django.contrib import admin

# Register your models here.
from home.models import Store, Product, Sales

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.resgister(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    pass