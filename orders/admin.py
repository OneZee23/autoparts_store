from django.contrib import admin

from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'autopart_url', 'count', )
    list_display_links = ('user_id', 'autopart_url')
    search_fields = ('autopart', 'count', )
    list_per_page = 25

admin.site.register(Order, OrderAdmin)