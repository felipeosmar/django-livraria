from django.db import models
from utils.models import BaseModel
from senai_testes.management.models import BrazilianState

# Create your models here.


class SexType(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"
    OTHER = "OTHER", "Other"


class Books(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Título")
    publishing_company = models.ForeignKey(
        "PublishingCompany", on_delete=models.CASCADE, verbose_name="Editora")
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, verbose_name="Autor")
    pages = models.IntegerField(verbose_name="Páginas")
    price = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Preço")
    publication_date = models.DateField(verbose_name="Data de Publicação")

    def __str__(self):
        return f"Livro | {self.title}"

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"


class Author(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Nome")
    last_name = models.CharField(max_length=100, verbose_name="Sobrenome")
    sex = models.CharField(
        max_length=10, choices=SexType.choices, verbose_name="Sexo")
    birth_date = models.DateField(verbose_name="Data de Nascimento")

    def __str__(self):
        return f"Autor | {self.name} {self.last_name}"

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class PublishingCompany(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Nome")
    cnpj = models.CharField(max_length=20, verbose_name="CNPJ")
    address = models.CharField(
        help_text="Endereço oficial", verbose_name="Endereço", max_length=100
    )
    address_number = models.CharField("Número", max_length=50)
    address_complement = models.CharField(
        "Complemento", max_length=1000, null=True, blank=True
    )
    city = models.CharField(
        help_text="Cidade", verbose_name="Cidade", max_length=50)
    state = models.CharField(
        help_text="Estado da federação",
        verbose_name="Estado",
        max_length=2,
        choices=BrazilianState.choices,
    )
    zipcode = models.CharField(help_text="CEP", max_length=20)

    def __str__(self):
        return f"Editora | {self.name}"

    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"


class BookStock(BaseModel):
    book = models.ForeignKey(
        "Books", on_delete=models.CASCADE, verbose_name="Livro")
    quantity = models.IntegerField(verbose_name="Quantidade")
    price = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Preço")

    def __str__(self):
        return f"Estoque | {self.book.title}"

    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"
