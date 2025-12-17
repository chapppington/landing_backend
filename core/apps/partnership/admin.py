from django.contrib import admin
from django.utils.html import format_html

from .models import PartnershipModel


@admin.register(PartnershipModel)
class PartnershipAdmin(admin.ModelAdmin):
    """Админка для управления карточками партнерства"""

    list_display = ["image_preview", "title", "order", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title", "description"]
    readonly_fields = ["image_preview", "created_at"]
    ordering = ["order", "title"]

    fieldsets = (
        (
            "Основная информация",
            {"fields": ("title", "description", "image", "image_preview")},
        ),
        ("Настройки", {"fields": ("order", "created_at")}),
    )

    def image_preview(self, obj):
        """Превью изображения в админке"""
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 150px; max-height: 100px; object-fit: cover; border-radius: 4px;" />',
                obj.image.url,
            )
        return "Нет изображения"

    image_preview.short_description = "Превью"
