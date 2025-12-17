from django.db import models


class RegistrationsModel(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя",
        help_text="Полное имя участника",
    )

    email = models.EmailField(verbose_name="Email", help_text="Адрес электронной почты")

    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон",
    )

    comments = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="Комментарий",
    )

    consent = models.BooleanField(
        default=False,
        verbose_name="Согласие на обработку данных",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации",
    )

    class Meta:
        db_table = "registrations"
        verbose_name = "Регистрация"
        verbose_name_plural = "Регистрации"
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.name} ({self.email}) - {self.created_at.strftime('%d.%m.%Y %H:%M')}"
        )
