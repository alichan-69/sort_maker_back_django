from django.contrib import admin

from .models import Sort


@admin.register(Sort)
class SortAdmin(admin.ModelAdmin):
    pass
