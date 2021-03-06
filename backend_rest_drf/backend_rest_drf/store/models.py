from django.db.models.fields import PositiveSmallIntegerField
from django.utils.translation import gettext_lazy as _
from django.db import models
import uuid


class Store(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"))
    rating = models.PositiveSmallIntegerField(_("Rating"))

    def __str__(self):
        return f'{self.name} - {self.id}'


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    storeId = models.ForeignKey(Store, verbose_name=_(
        "Store"), on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self):
        return f'{self.name} - {self.id}'


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoryId = models.ForeignKey(Category, verbose_name=_(
        "Category"), on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=50)
    price = models.PositiveIntegerField(_("Price"))

    def __str__(self):
        return f'{self.name} - {self.id}'
