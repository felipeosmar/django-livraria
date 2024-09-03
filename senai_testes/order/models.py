from django.db import models
from utils.models import BaseModel
from senai_testes.management.models import Client, Seller
from senai_testes.books.models import Books

# Create your models here.


class Order(BaseModel):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, verbose_name="Cliente")
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, verbose_name="Vendedor")
    total = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Total")
    status = models.CharField(max_length=20, verbose_name="Status")
    order_date = models.DateField(verbose_name="Data do Pedido")

    def __str__(self):
        return f'Pedido | {self.client.user.name}'


class OrderItem(BaseModel):
    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, verbose_name="Pedido")
    book = models.ForeignKey(
        Books, on_delete=models.CASCADE, verbose_name="Livro")
    quantity = models.IntegerField(verbose_name="Quantidade")
    price = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Preço")

    def __str__(self):
        return f'Item de Pedido | {self.book.title}'

    class Meta:
        verbose_name = "Item de Pedido"
        verbose_name_plural = "Itens de Pedido"
