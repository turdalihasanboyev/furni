from django.contrib import admin

from .models import SubEmail


admin.site.site_header = "furni Admin Dashboard"
admin.site.site_title = "furni Admin Dashboard"
admin.site.index_title = "Welcome to furni Admin Dashbord!"


@admin.register(SubEmail)
class SubEmailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'created_at',
        'updated_at',
    )
    search_fields = ('email', 'name',)
    list_filter = ('is_active',)
