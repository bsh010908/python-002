from django.contrib import admin
from .models import ShippingPort, Ship

@admin.register(ShippingPort)
class ShippingPortAdmin(admin.ModelAdmin):
    list_display = ("country", "port", "lat", "lon")  # ✅ Grid 형태
    search_fields = ("country", "port")
    list_filter = ("country",)


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "lat", "lon")  # ✅ Grid 형태
    search_fields = ("name", "status")
    list_filter = ("status",)
