from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'created_at',
        'updated_at',
    )
    search_fields = ('first_name', 'last_name', 'email',)
