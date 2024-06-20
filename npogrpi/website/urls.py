from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name ='catalog'),
    path('catalog/<slug:type_slug>/', views.type_product, name = 'type_product'),
    path('catalog/<slug:type_slug>/<slug:product_slug>/', views.product_card, name='product_card'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('politico/', views.PoliticoStaticPage.as_view(), name = 'politico'),
]