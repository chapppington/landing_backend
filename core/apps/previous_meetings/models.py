from django.db import models


class PreviousMeetingsModel(models.Model):
    image = models.ImageField(
        upload_to="previous_meetings/",
        verbose_name="Фото",
        help_text="Фотография с предыдущей встречи",
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Порядок отображения",
        help_text="Порядок сортировки фотографий",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания",
    )

    class Meta:
        db_table = "previous_meetings"
        verbose_name = "Предыдущая встреча"
        verbose_name_plural = "Предыдущие встречи"
        ordering = ["order", "-created_at"]

    def __str__(self):
        return f"Фото #{self.id} - {self.created_at.strftime('%d.%m.%Y')}"
