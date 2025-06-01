from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Contact(BaseModel):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.full_name}"
