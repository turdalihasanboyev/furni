from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering = ('email',)
    search_fields = ('email',)
    list_display = (
        'id',
        'email',
        'is_active',
        'is_superuser',
        'is_staff',
        'last_login',
        'date_joined',
    )
    readonly_fields = (
        'id',
        'last_login',
        'date_joined',
    )
    list_filter = (
        'is_active',
        'is_superuser',
        'is_staff',
    )
    fieldsets = (
        ('Login', {
            'fields': ('email', 'password',),
            'classes': ('wide',),
        }),
        ("Permissions", {
            'fields': ('is_superuser', 'is_staff', 'is_active',),
            'classes': ('wide',),
        }),
        ("Important Dates", {
            'fields': ('date_joined', 'last_login',),
            'classes': ('wide', 'collapse',),
        }),
        ("ID", {
            'fields': ('id',),
            'classes': ('wide', 'collapse',),
        }),
    )
    add_fieldsets = (
        ('Create Super User', {
            'fields': ('email', 'password1', 'password2',),
            'classes': ('wide',),
        }),
        ("Permissions", {
            'fields': ('is_superuser', 'is_staff',),
            'classes': ('wide',),
        }),
    )
