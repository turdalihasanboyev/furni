from django.contrib import admin

from .models import Testimonial, Agent


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'image',
        'job',
        'created_at',
        'updated_at',
    )
    search_fields = ('full_name', 'job',)


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'image',
        'job',
        'created_at',
        'updated_at',
    )
    search_fields = ('full_name', 'job',)
