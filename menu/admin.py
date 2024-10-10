from django.contrib import admin
from menu.models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'url', 'named_url')
    list_filter = ('name',)
    search_fields = ('name', 'url', 'named_url')
    ordering = ('name',)


admin.site.register(MenuItem, MenuItemAdmin)
