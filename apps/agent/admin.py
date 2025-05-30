from django.contrib import admin

from .models import Agent


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'role',
        'full_name',
        'image',
        'job',
        'created_at',
        'updated_at',
    )
    search_fields = ('full_name', 'job',)
    list_filter = ('role',)
