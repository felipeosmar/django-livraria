from django.contrib import admin
from .models import Books, Author, PublishingCompany, BookStock
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "publishing_company",
                    "author", "pages", "price", "publication_date"]


admin.site.register(Books, BooksAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "last_name", "sex", "birth_date"]


admin.site.register(Author, AuthorAdmin)


class PublishingCompanyAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "cnpj", "address", "address_number",
                    "address_complement", "city", "state", "zipcode"]


admin.site.register(PublishingCompany, PublishingCompanyAdmin)


class BooksStockAdmin(admin.ModelAdmin):
    list_display = ["id", "book", "quantity", "price"]


admin.site.register(BookStock, BooksStockAdmin)
