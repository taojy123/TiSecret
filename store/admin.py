from django.contrib import admin

from store import models


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'updated_at', 'created_at']
    list_filter = ['user']

