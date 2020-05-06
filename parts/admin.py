from django.contrib import admin
from .models import Category, Automake, Autopart

class ListingAutopart(admin.ModelAdmin):
    list_display = ('title', 'count', 'category', 'draft', 'price')
    list_display_links = ('title', 'count')
    list_filter = ('category', 'count')
    list_editable = ('draft',)
    search_fields = ('title', 'description')
    list_per_page = 25

admin.site.register(Category)
admin.site.register(Automake)
admin.site.register(Autopart, ListingAutopart)