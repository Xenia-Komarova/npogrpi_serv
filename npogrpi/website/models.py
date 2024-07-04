from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


class MainPage(models.Model):
    main_image = models.ImageField(upload_to='media/website/',
                                   help_text='Изображение для главной страницы',
                                   blank=True,
                                   )
    about = models.TextField(help_text='Описание компании на главной странице',
                             verbose_name='Описание краткое',
                             )
    about_en = models.TextField(help_text='Short description on main page',
                             verbose_name='Short description',
                             blank=True,
                             null=True,
                             )
    main_title = models.CharField(help_text='Заголовок и meta',
                                  verbose_name='Заголовок главной страницы',
                                  max_length=250,
                                  )
    main_title_en = models.CharField(help_text='Title and meta tag',
                                  verbose_name='Title of main page and meta tag',
                                  max_length=250,
                                  blank=True,
                                  null=True,
                                  )
    
    def __str__(self):
       return self.main_title
    
    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    
class Partner(models.Model):
    name = models.CharField(help_text='Наименование партнера',
                            verbose_name='Название партера',
                            max_length=150,
                            )
    image = models.ImageField(upload_to='media/website/',
                              help_text='Логотип партнера',
                              height_field=None, 
                              width_field=None, 
                              max_length=None,
                              blank=True,
                              )
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Наш партнёр'
        verbose_name_plural = 'Наши партнёры'

class Advantages(models.Model):
    name = models.CharField(help_text='Заголовок',
                            verbose_name='Наименование преимущества',
                            max_length=100,
                            )
    name_en = models.CharField(help_text='Title',
                            verbose_name='Advantages title',
                            max_length=100,
                            blank=True,
                            null=True,
                            )
    text = models.TextField(help_text='Описание',
                            verbose_name='Описание преимущества',
                            )
    text_en = models.TextField(help_text='Description',
                            verbose_name='Description of advatages',
                            blank=True,
                            null=True,
                            )
    image = models.ImageField(upload_to='media/advantages/',
                              help_text='Загрузите иконку',
                              verbose_name='Изображение преимущества',
                              )
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name= 'Наше преимущество'
        verbose_name_plural = 'Наши преимущества'

class About(models.Model):
    text = HTMLField(verbose_name='Описание компании',
                            help_text='Текст о компании',
                            )
    text_en = HTMLField(verbose_name='Descrteion company',
                            help_text='About company full descrintion',
                            blank=True,
                            null=True,
                            )
    title = models.CharField(verbose_name='Заголовок',
                             max_length=250,
                             )
    title_en = models.CharField(verbose_name='Title',
                             max_length=250,
                             blank=True,
                             null=True,
                             )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class Contacts(models.Model):
    email = models.EmailField(verbose_name='e-mail для связи',
                              help_text='e-mail для связи c контактным лицом',
                              )
    telephone = models.CharField(verbose_name='контактный телефон',
                                 help_text='контактный телефон',
                                 max_length=15,
                                 )
    adress = models.TextField(verbose_name='адрес комапании',
                              help_text='почтовый адрес',
                              blank=True,
                              null=True
                            )
    adress_en = models.TextField(verbose_name='Adress',
                              help_text='Post adress',
                              blank=True,
                              null=True
                            )
    
    def __str__(self) -> str:
        return self.adress
    
    class Meta:
        verbose_name= 'Контакт'
        verbose_name_plural = 'Контакты'


class Type(models.Model):
    name = models.CharField(max_length=300,
                            verbose_name='Тип оборудования',
                            )
    name_en = models.CharField(max_length=300,
                            verbose_name='Type',
                            blank=True,
                            null=True
                            )
    slug = models.SlugField(max_length=300,
                            unique=True,
                            db_index=True,
                            verbose_name='URL',
                            )
    image = models.ImageField(verbose_name='Изображение',
                              upload_to='media/img/type/',
                              help_text='Добавьте файл c изображением',
                              )
    inmgrp = models.BooleanField(default=False,
                                 verbose_name='Оборудование входит в комплект',
                                 )
    incalc = models.BooleanField(default=False,
                                 verbose_name='Включить в калькулятор',
                                 )
    public = models.BooleanField(default=False,
                                 verbose_name='Опубликовано',
                                 )
    seo_description = models.CharField(max_length=160,
                                       verbose_name='Описание для поисковиков, <160 символов',
                                       )
    seo_keywords = models.CharField(max_length=300,
                                    verbose_name='ключевые слова через запятую <10',
                                    )
    created = models.DateField(auto_now_add=True,
                               verbose_name="Создано",)
    updated = models.DateField(auto_now=True,
                               verbose_name="Обновлено",)
    
    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудования'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('type_product', kwargs={'type_slug': self.slug})


class DiameterShank(models.Model):
    meaning = models.IntegerField(verbose_name='Значение')

    def __str__(self):
        return str(self.meaning)

    class Meta:
        verbose_name = 'Условный диаметр хвостовика'
        verbose_name_plural = 'Условный диаметр хвостовика'
    

class DiameterColumn(models.Model):
    meaning = models.IntegerField(verbose_name='Значение', 
                                  default=None,)

    def __str__(self):
        return str(self.meaning)

    class Meta:
        verbose_name = 'Условный диаметр колонны'
        verbose_name_plural = 'Условный диаметр колонны'
    

class DiameterOpenBorehole(models.Model):
    meaning = models.DecimalField(max_digits=5,
                                  decimal_places=1,
                                  verbose_name='Значение')
    
    def __str__(self):
        return str(self.meaning)

    class Meta:
        verbose_name = 'Диаметр открытого ствола'
        verbose_name_plural = 'Диаметр открытого ствола'


class Product(models.Model):
    name = models.CharField(max_length=300,
                            verbose_name='Наименование оборудования',
                            )
    name_en = models.CharField(max_length=300,
                            verbose_name='Product name',
                            blank=True,
                            null=True,
                            )
    type = models.ForeignKey(Type, 
                             verbose_name='Тип оборудования', 
                             on_delete=models.CASCADE,
                             related_name='products',
                             )
    description = HTMLField(verbose_name='Описание')
    description_en = HTMLField(verbose_name='Описание',
                               blank=True,
                               null=True,
                               )
    image = models.ImageField(verbose_name='Изображение',
                              upload_to='media/img/product/',
                              help_text='Добавьте файл c изображением'
                              )
    price = models.FloatField(verbose_name='Цена')
    slug = models.SlugField(max_length=300,
                            db_index=True,
                            verbose_name='URL')
    diameter_column = models.ManyToManyField(DiameterColumn,
                                            verbose_name='Условный диаметр колонны',
                                            related_name='diameter_column',
                                            )
    diameter_shank = models.ManyToManyField(DiameterShank,
                                            verbose_name='Условный диаметр хвостовика',
                                            related_name='diameter_shank',
                                            )
    diameter_open_borehole = models.ManyToManyField(DiameterOpenBorehole,
                                            verbose_name='Диаметр открытого ствола',
                                            related_name='diameter_open_borehole',
                                            )
    fitting_outer_diameter = models.DecimalField(verbose_name='Наружный диаметр оснастки, мм',
                                                 max_digits=10,
                                                 decimal_places=2,
                                                 blank=True,
                                                 default=1.00
                                                 )
    fitting_inner_diameter = models.DecimalField(verbose_name='Внутренний диаметр оснастки',
                                                 max_digits=10,
                                                 decimal_places=2,
                                                 blank=True,
                                                 default=1.00
                                                 )
    fitting_length = models.DecimalField(verbose_name='Длина оснастки',
                                         max_digits=10,
                                         decimal_places=2,
                                         blank=True,
                                         default=1.00
                                         )
    incalc = models.BooleanField(default=False,
                                 verbose_name='Включить в калькулятор',
                                 )
    public = models.BooleanField(default=False,
                                 verbose_name='Опубликовано',
                                 )
    seo_description = models.CharField(max_length=160,
                                       verbose_name='Описание для поисковиков, <160 символов',
                                       )
    seo_keywords = models.CharField(max_length=300,
                                    verbose_name='ключевые слова через запятую <10',
                                    )
    created = models.DateField(auto_now_add=True,
                               verbose_name="Создано",)
    updated = models.DateField(auto_now=True,
                               verbose_name="Обновлено",)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_card', kwargs={'product_slug': self.slug})
    
    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        

class PriceProduct(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE
                                )
    meaning = models.DecimalField(max_digits=8, 
                                  decimal_places=2
                                  )
    monetary_unit = models.CharField(max_length=5,
                                    verbose_name='Денежная единица',
                                    )
    def __str__(self) -> str:
        return {self.product} - {self.meaning}
    
    class Meta:
        verbose_name = 'Стоимость продукции'
        verbose_name_plural = 'Стоимость продукции'
