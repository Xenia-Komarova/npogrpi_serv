from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Contact(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.email


class MenuItem(MPTTModel):
    name = models.CharField(max_length=100,
                            unique=True,
                            )
    name_en = models.CharField(max_length=100, 
                               blank=True,
                               null=True,
                               )
    url = models.CharField('Ссылка', max_length=255)
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'