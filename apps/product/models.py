from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Product(BaseModel):
    PRICE_TYPE = (
        ("USD", '$'),
        ("EUR", '€'),
        ("RUB", '₽'),
        ("UZS", "so'm"),
    )

    name = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    percentage = models.PositiveIntegerField(default=0)
    price_type = models.CharField(max_length=10, choices=PRICE_TYPE, default='USD')

    @property
    def discount_price(self):
        discount = (self.price * self.percentage) / 100
        return self.price - discount

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return f'{self.name}'
