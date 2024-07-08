from django.db import models
from django.utils.translation import gettext_lazy as _



class ContactSearch(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name=_('Имя'),
                            )
    phone_number = models.CharField(max_length=20,
                                    verbose_name=_('Телефон'),
                                    )
    email = models.EmailField()
    company = models.CharField(max_length=100,
                               verbose_name=_('Компания'),
                               )

    def __str__(self):
        return self.name
