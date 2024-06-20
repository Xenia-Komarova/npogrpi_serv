from django.contrib import admin
from tinymce.widgets import TinyMCE

from .models import (About, Advantages, Contacts, DiameterColumn,
                     DiameterOpenBorehole, DiameterShank, MainPage, Partner,
                     Product, Type)


class MainPageAdmin(admin.ModelAdmin):
    list_display = (
        'main_image',
        'about',
        'main_title',
        )
    empty_value_display = '-пусто-'


class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    empty_value_display = '-пусто-'


class AdvantagesAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'text',
    )
    empty_value_display = '-пусто-'


class AdoutAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
    )
    widget=TinyMCE(attrs={'cols': 80, 'rows': 30})
    empty_value_display = '-пусто-'


class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        'adress',
        'email',
        'telephone',
    )
    empty_value_display = '-пусто-'


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'slug',
        'incalc',
        'public',
    )
    list_filter = ('name', 'incalc', 'public',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name", )}
    empty_value_display = '-пусто-'


class DiameterColumnAdmin(admin.ModelAdmin):
    list_display = (
    'meaning',
    )

class DiameterOpenBoreholeAdmin(admin.ModelAdmin):
    list_display = (
    'meaning',
    )

class DiameterShankAdmin(admin.ModelAdmin):
    list_display = (
    'meaning',
    )

class РroductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'slug',
        'price',
        'incalc',
        'public',
    )
    list_filter = ('name', 'type', 'incalc', 'public',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name", )}
    filter_horizontal = ('diameter_column', 'diameter_open_borehole', 'diameter_shank')


admin.site.register(MainPage, MainPageAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Advantages, AdvantagesAdmin)
admin.site.register(About, AdoutAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Product, РroductAdmin)
admin.site.register(DiameterColumn, DiameterColumnAdmin)
admin.site.register(DiameterOpenBorehole, DiameterOpenBoreholeAdmin)
admin.site.register(DiameterShank, DiameterShankAdmin)

