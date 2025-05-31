from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Agent(BaseModel):
    class Role(models.TextChoices):
        AGENT = 'agent', 'Agent'
        TESTIMONIAL = 'testimonial', 'Testimonial'

    role = models.CharField(max_length=50, choices=Role.choices, default=Role.AGENT)
    full_name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='agent_images', null=True, blank=True)
    job = models.CharField(max_length=225)
    description = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'

    def __str__(self):
        return f'{self.full_name}'
