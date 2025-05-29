from django.contrib import admin

from .models import Testimonial, Agent


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'image',
        'job',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = ('full_name', 'job',)
    list_filter = ('is_active',)


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'image',
        'job',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = ('full_name', 'job',)
    list_filter = ('is_active',)
