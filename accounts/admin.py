from django.contrib import admin

from .models import User_Panel

class UserAdmin(admin.ModelAdmin):
    list_display = ("panel_id", "first_name", "email")

admin.site.register(User_Panel, UserAdmin)