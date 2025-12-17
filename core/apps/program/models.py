from django.db import models


class ProgramModel(models.Model):
    time = models.CharField(
        max_length=50,
        verbose_name="Время",
        help_text="Время проведения мероприятия (например: 09:00 – 09:30)",
    )

    title = models.CharField(
        max_length=500,
        verbose_name="Название",
        help_text="Название мероприятия",
    )

    moderator = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Модератор",
        help_text="Модератор мероприятия (опционально)",
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Порядок отображения",
        help_text="Порядок сортировки мероприятий",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания",
    )

    class Meta:
        db_table = "program"
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ["order", "time"]

    def __str__(self):
        return f"{self.time} - {self.title}"
