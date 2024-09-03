from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ["client", "seller", "total", "status", "order_date"]
    search_fields = ["client", "seller", "status", "order_date"]
    list_filter = ["status", "order_date"]


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "book", "quantity", "price"]
    search_fields = ["order", "book", "quantity", "price"]
    list_filter = ["quantity", "price"]


admin.site.register(OrderItem, OrderItemAdmin)
