from django.contrib import admin

from .models import Sort, SortItem


@admin.register(Sort)
class SortAdmin(admin.ModelAdmin):
    pass


@admin.register(SortItem)
class SortAdmin(admin.ModelAdmin):
    pass
