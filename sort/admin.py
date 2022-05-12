from django.contrib import admin

from .models import User, Sort, SortItem, Like


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Sort)
class SortAdmin(admin.ModelAdmin):
    pass


@admin.register(SortItem)
class SortAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
