from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Product, Type


class StaticSitemap(Sitemap):
    """
    Карта-сайта для статичных страниц
    """
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return ['website:index', 'website:about', 'website:contacts', 'website:catalog']
    
    def location(self, item):
        return reverse(item)

class TypeProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Type.objects.all().order_by('name')

    def location(self, item):
        return reverse('website:type_product', kwargs={'type_slug': item.slug})
    
    def lastmod(self, item):
        return item.updated

class ProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Product.objects.all().order_by('name')

    def location(self, item):
        return reverse('website:product_card', kwargs={
                                                    'type_slug': item.type.slug,
                                                    'product_slug': item.slug})
    def lastmod(self, item):
        return item.updated