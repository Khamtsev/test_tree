from django.db import models
from django.urls import reverse
from menu.constants import (MENU_NAME_MAX_LENGTH,
                            MENU_NAMED_URL_MAX_LENGTH,
                            MENU_URL_MAX_LENGTH)


class MenuItem(models.Model):
    name = models.CharField(
        'Название меню',
        max_length=MENU_NAME_MAX_LENGTH,
        unique=True
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name='Предок'
    )
    url = models.CharField(
        'URL',
        max_length=MENU_URL_MAX_LENGTH,
        blank=True,
        null=True
    )
    named_url = models.CharField(
        'Named URL',
        max_length=MENU_NAMED_URL_MAX_LENGTH,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'меню'

    def __str__(self):
        return self.name

    def get_url(self):
        if self.url:
            return self.url
        elif self.named_url:
            return reverse(self.named_url)
        else:
            return
