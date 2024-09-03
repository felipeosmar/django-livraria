from django.contrib import admin
from senai_testes.management.models import (
    User, Client, Seller
)
from django.contrib.auth.hashers import make_password

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active", "is_superuser"]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

    def get_fieldsets(self, request, obj=None):
        if obj:
            return [(None, {"fields": ("name", "email", "is_active")})]
        return [
            (None, {"fields": ("name", "email", "password", "is_active")})
        ]

    def save_model(self, request, obj, form, change):
        if "password" in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "cpf", "phone", "address",
                    "address_number", "address_complement", "city", "state", "zipcode"]


admin.site.register(Client, ClientAdmin)


class SellerAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "cpf", "phone"]


admin.site.register(Seller, SellerAdmin)
