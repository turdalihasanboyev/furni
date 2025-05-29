from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SubEmail(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(unique=True, max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Sub Email'
        verbose_name_plural = 'Sub Emails'

    def __str__(self):
        return f'{self.name} - {self.email}'
