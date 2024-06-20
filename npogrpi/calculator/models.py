from django.db import models


class ContactSearch(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Имя',
                            )
    phone_number = models.CharField(max_length=20,
                                    verbose_name='Телефон',
                                    )
    email = models.EmailField()
    company = models.CharField(max_length=100,
                               verbose_name='Компания',
                               )

    def __str__(self):
        return self.name
