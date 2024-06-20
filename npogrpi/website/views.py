from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView

from core.forms import ContactForm
from core.views import contact_view

from .models import (About, Advantages, Contacts, MainPage, Partner, Product,
                     Type)


def index(request):

    page_obj = MainPage.objects.all()
    partners = Partner.objects.all()
    advantages = Advantages.objects.all()
    context = {
        'page_obj': page_obj,
        'partners': partners,
        'advantages': advantages,
    }

    return render(request, 'website/index.html', context)


def catalog(request):
    
    page_obj = Type.objects.filter(public__in=[True])
    context = {
        'page_obj': page_obj,
    }

    return render(request, 'website/catalog.html', context)


def type_product(request, type_slug):

    type_instance = get_object_or_404(Type, slug=type_slug)
    product_list = type_instance.products.filter(public__in=[True])
    context = {
        'type_instance': type_instance,
        'product_list': product_list,
    }

    return render(request, 'website/type_product.html', context)


def product_card(request, type_slug, product_slug):

    product = get_object_or_404(Product, slug=product_slug)
    context = {
        'product':product,
        'type_slug': type_slug,
    }

    return render(request, 'website/product_card.html', context)


def about(request):

    page_obj = About.objects.all()
    advantages = Advantages.objects.all()
    partners = Partner.objects.all()
    context = {
        'page_obj': page_obj,
        'advantages': advantages,
        'partners': partners,
    }

    return render(request, 'website/about.html', context)


def contacts(request):

    page_obj = Contacts.objects.all()
    form = ContactForm()
    contact_view(request)
    context = {
        'page_obj': page_obj,
        'form':form,
    }

    return render(request, 'website/contacts.html', context)


class PoliticoStaticPage(TemplateView):
    # В переменной template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница
    template_name = 'website/politico.html' 

