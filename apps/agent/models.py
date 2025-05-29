from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Testimonial(BaseModel):
    full_name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='testimonial_images', null=True, blank=True)
    job = models.CharField(max_length=225)
    testimonial = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f'{self.full_name}'


class Agent(BaseModel):
    full_name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='agent_images', null=True, blank=True)
    job = models.CharField(max_length=225)
    description = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'

    def __str__(self):
        return f'{self.full_name}'
