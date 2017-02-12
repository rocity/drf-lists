from django.contrib import admin

from .models import Item, List


class ItemAdmin(admin.ModelAdmin):
    pass


class ListAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)
admin.site.register(List, ListAdmin)
