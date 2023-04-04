from django.db import models


class CreatedModel(models.Model):
    """Абстрактная модель. Добавляет дату и время создания"""
    pub_date = models.DateTimeField(
        verbose_name='Дата и время создания',
        help_text='Дата и время вносятся автоматически',
        auto_now_add=True,
    )

    class Meta:
        abstract = True
