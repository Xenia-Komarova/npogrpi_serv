from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils.translation import get_language, activate, LANGUAGE_SESSION_KEY
from django.views.generic.base import TemplateView

from core.forms import ContactForm
from core.views import contact_view

from .models import (About, Advantages, Contacts, MainPage, Partner, Product,
                     Type)


def index(request):

    current_language = get_language()
    page_obj = get_object_or_404(MainPage)
    partners = Partner.objects.all()
    advantages = Advantages.objects.all()
    
    if current_language == 'en':
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
    switch_lang_url = reverse('website:index') + '?lang=' + ('ru' if current_language == 'en' else 'en')
    #print(f'Switch language URL: {switch_lang_url}')
    
    lang = request.GET.get('lang')
    if lang and lang != current_language:
        activate(lang)
    #    print(f'Activated language: {lang}')
        request.session[LANGUAGE_SESSION_KEY] = lang
        return redirect(reverse('website:index'))
    if LANGUAGE_SESSION_KEY in request.session:
        activate(request.session[LANGUAGE_SESSION_KEY])
        current_language = request.session[LANGUAGE_SESSION_KEY]
    
    context = {
        'request': request,
        'page_obj': page_obj,
        'partners': partners,
        'advantages': advantages,
        'current_language': current_language,
        'switch_lang_url': switch_lang_url,
    }
    #print(f'Redirecting to: {reverse("website:index")}')

    return render(request, 'website/index.html', context)


def catalog(request):
    
    current_language = get_language()
    page_obj = Type.objects.filter(public__in=[True])
    if current_language == 'en':
        for odj in page_obj:
            odj.display_name = odj.name_en
    else:
        for odj in page_obj:
            odj.display_name = odj.name
    switch_lang_url = reverse('website:catalog') + '?lang=' + ('ru' if current_language == 'en' else 'en')
    lang = request.GET.get('lang')
    if lang and lang != current_language:
        activate(lang)
        return redirect(reverse('website:catalog'))
    if LANGUAGE_SESSION_KEY in request.session:
        activate(request.session[LANGUAGE_SESSION_KEY])
        current_language = request.session[LANGUAGE_SESSION_KEY]
    context = {
        'page_obj': page_obj,
        'current_language': current_language,
        'switch_lang_url': switch_lang_url,
    }

    return render(request, 'website/catalog.html', context)
#тут закончила

def type_product(request, type_slug):

    current_language = get_language()
    type_instance = get_object_or_404(Type, slug=type_slug)
    product_list = type_instance.products.filter(public__in=[True])
    if current_language == 'en':
        for odj in product_list:
            odj.display_name = odj.name_en
    else:
        for odj in product_list:
            odj.display_name = odj.name
    switch_lang_url = reverse('website:type_product') + '?lang=' + ('ru' if current_language == 'en' else 'en')
    lang = request.GET.get('lang')
    if lang and lang != current_language:
        activate(lang)
        return redirect(reverse('website:type_product'))
    context = {
        'type_instance': type_instance,
        'product_list': product_list,
        'switch_lang_url': switch_lang_url,
    }

    return render(request, 'website/type_product.html', context)


def product_card(request, type_slug, product_slug):

    current_language = get_language()
    product = get_object_or_404(Product, slug=product_slug)
    if current_language == 'en':
        product.display_name = product.name_en
        product.display_description = product.description_en
    else:
        product.display_name = product.name
        product.display_description = product.description
    switch_lang_url = reverse('website:product_card') + '?lang=' + ('ru' if current_language == 'en' else 'en')
    lang = request.GET.get('lang')
    if lang and lang != current_language:
        activate(lang)
        return redirect(reverse('website:product_card'))
    context = {
        'product':product,
        'type_slug': type_slug,
        'switch_lang_url': switch_lang_url,
    }

    return render(request, 'website/product_card.html', context)


def about(request):

    current_language = get_language()
    page_obj = About.objects.all()
    if current_language == 'en':
            page_obj.display_text = page_obj.text_en
            page_obj.display_title = page_obj.title_en
    else:
            page_obj.display_text = page_obj.text
            page_obj.display_title = page_obj.title
    switch_lang_url = reverse('website:about') + '?lang=' + ('ru' if current_language == 'en' else 'en')
    lang = request.GET.get('lang')
    if lang and lang != current_language:
        activate(lang)
        return redirect(reverse('website:about'))
    context = {
        'page_obj': page_obj,
        'switch_lang_url': switch_lang_url,
    }

    return render(request, 'website/about.html', context)


def contacts(request):

    current_language = get_language()
    page_obj = Contacts.objects.all()
    form = ContactForm()
    contact_view(request)
    if current_language == 'en':
            page_obj.display_adress = page_obj.adress_en
    else:
            page_obj.display_adress = page_obj.adress
    switch_lang_url = reverse('website:contacts') + '?lang=' + ('ru' if current_language == 'en' else 'en')
    lang = request.GET.get('lang')
    if lang and lang != current_language:
        activate(lang)
        return redirect(reverse('website:contacts'))
    context = {
        'page_obj': page_obj,
        'form':form,
        'switch_lang_url': switch_lang_url,
    }

    return render(request, 'website/contacts.html', context)


class PoliticoStaticPage(TemplateView):
    # В переменной template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница
    template_name = 'website/politico.html' 
