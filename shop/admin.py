from django.contrib import admin

from shop.models import Category, Product, Order, Customer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
