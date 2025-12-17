from django.contrib import admin

from .models import AboutModel


@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    """Админка для управления карточками 'О конференции'"""

    list_display = ["title", "order", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title", "description"]
    readonly_fields = ["created_at"]
    ordering = ["order", "title"]

    fieldsets = (
        ("Основная информация", {"fields": ("title", "description")}),
        ("Настройки", {"fields": ("order", "created_at")}),
    )
