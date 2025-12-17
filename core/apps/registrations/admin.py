from django.contrib import admin

from .models import RegistrationsModel


@admin.register(RegistrationsModel)
class RegistrationAdmin(admin.ModelAdmin):
    """Админка для управления регистрациями"""

    list_display = ["name", "email", "phone", "consent", "created_at"]
    list_filter = ["consent", "created_at"]
    search_fields = ["name", "email", "phone"]
    readonly_fields = ["created_at"]
    ordering = ["-created_at"]

    fieldsets = (
        ("Основная информация", {"fields": ("name", "email", "phone")}),
        ("Дополнительно", {"fields": ("comments", "consent", "created_at")}),
    )
