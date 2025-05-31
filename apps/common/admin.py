from django.contrib import admin

from .models import SubEmail


admin.site.site_header = "Furni Admin Dashboard"
admin.site.site_title = "Furni Admin Dashboard"
admin.site.index_title = "Welcome to Furni Admin Dashbord!"


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
