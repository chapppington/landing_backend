from django.db import models


class SpeakersModel(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя",
    )

    position = models.CharField(
        max_length=255,
        verbose_name="Должность",
    )

    image = models.ImageField(
        upload_to="speakers/",
        blank=True,
        null=True,
        verbose_name="Фото",
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Порядок отображения",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    class Meta:
        db_table = "speakers"
        verbose_name = "Спикер"
        verbose_name_plural = "Спикеры"
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.name} - {self.position}"
