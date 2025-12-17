from django.db import models


class PartnershipModel(models.Model):
    title = models.CharField(
        max_length=500,
        verbose_name="Заголовок",
        help_text="Заголовок карточки",
    )

    description = models.TextField(
        max_length=1000,
        verbose_name="Описание",
        help_text="Описание карточки",
    )

    image = models.ImageField(
        upload_to="partnership/",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Изображение для карточки партнерства (опционально)",
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Порядок отображения",
        help_text="Порядок сортировки карточек",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания",
    )

    class Meta:
        db_table = "partnership"
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"
        ordering = ["order", "title"]

    def __str__(self):
        return self.title
