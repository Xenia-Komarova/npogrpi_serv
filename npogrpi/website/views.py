from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.translation import get_language
from django.views.generic.base import TemplateView

from core.forms import ContactForm
from core.views import contact_view

from .models import (About, Advantages, Contacts, MainPage, Partner, Product,
                     Type)


def index(request):
    page_obj = get_object_or_404(MainPage)
    partners = Partner.objects.all()
    advantages = Advantages.objects.all()
    
    if get_language() == 'en':
        page_obj.display_about = page_obj.about_en
        page_obj.display_main_title = page_obj.main_title_en
        for adv in advantages:
            adv.display_name = adv.name_en
            adv.display_text = adv.text_en
    else:
        page_obj.display_about = page_obj.about
        page_obj.display_main_title = page_obj.main_title
        for adv in advantages:
            adv.display_name = adv.name
            adv.display_text = adv.text_en 
    context = {
        'page_obj': page_obj,
        'partners': partners,
        'advantages': advantages,
    }

    return render(request, 'website/index.html', context)


def catalog(request):
    page_obj = Type.objects.filter(public__in=[True])
    if get_language() == 'en':
        for odj in page_obj:
            odj.display_name = odj.name_en
    else:
        for odj in page_obj:
            odj.display_name = odj.name
    context = {
        'page_obj': page_obj,
    }

    return render(request, 'website/catalog.html', context)
#тут закончила

def type_product(request, type_slug):

    type_instance = get_object_or_404(Type, slug=type_slug)
    product_list = type_instance.products.filter(public__in=[True])
    if get_language() == 'en':
        for odj in product_list:
            odj.display_name = odj.name_en
    else:
        for odj in product_list:
            odj.display_name = odj.name
    context = {
        'type_instance': type_instance,
        'product_list': product_list,
    }

    return render(request, 'website/type_product.html', context)


def product_card(request, type_slug, product_slug):

    product = get_object_or_404(Product, slug=product_slug)
    if get_language() == 'en':
        product.display_name = product.name_en
        product.display_description = product.description_en
    else:
        product.display_name = product.name
        product.display_description = product.description
    context = {
        'product':product,
        'type_slug': type_slug,
    }

    return render(request, 'website/product_card.html', context)


def about(request):

    page_obj = About.objects.all()
    if get_language() == 'en':
            page_obj.display_text = page_obj.text_en
            page_obj.display_title = page_obj.title_en
    else:
            page_obj.display_text = page_obj.text
            page_obj.display_title = page_obj.title

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'website/about.html', context)


def contacts(request):

    page_obj = Contacts.objects.all()
    form = ContactForm()
    contact_view(request)
    if get_language() == 'en':
            page_obj.display_adress = page_obj.adress_en
    else:
            page_obj.display_adress = page_obj.adress
    context = {
        'page_obj': page_obj,
        'form':form,
    }

    return render(request, 'website/contacts.html', context)


class PoliticoStaticPage(TemplateView):
    # В переменной template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница
    template_name = 'website/politico.html' 
