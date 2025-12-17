from django.contrib import admin

from .models import ProgramModel


@admin.register(ProgramModel)
class ProgramAdmin(admin.ModelAdmin):
    """Админка для управления программой"""

    list_display = ["time", "title", "moderator", "order", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title", "moderator"]
    readonly_fields = ["created_at"]
    ordering = ["order", "time"]

    fieldsets = (
        ("Основная информация", {"fields": ("time", "title", "moderator")}),
        ("Настройки", {"fields": ("order", "created_at")}),
    )
