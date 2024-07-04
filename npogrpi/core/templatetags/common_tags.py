from django import template
from django.shortcuts import redirect
from django.utils.translation import get_language, activate, LANGUAGE_SESSION_KEY
from django.urls import reverse

from core.models import MenuItem

register = template.Library()


@register.inclusion_tag('includes/menu.html', takes_context=True)
def show_menu(context):
    request = context['request']
    current_language = get_language()
    menu_items = MenuItem.objects.filter(level=1)
    
    for item in menu_items:
        if current_language == 'en':
            item.display_name = item.name_en
        else:
            item.display_name = item.name
    
    switch_lang_url = request.get_full_path() + '?lang=' + ('ru' if current_language == 'en' else 'en')
    lang = request.GET.get('lang')
    if lang and lang != current_language:
        activate(lang)
        request.session[LANGUAGE_SESSION_KEY] = lang
        return redirect(request.path_info)
    if LANGUAGE_SESSION_KEY in request.session:
        activate(request.session[LANGUAGE_SESSION_KEY])
        current_language = request.session[LANGUAGE_SESSION_KEY]
    return {
        'menu_items': menu_items,
        'current_language': current_language,
        'switch_lang_url': switch_lang_url,
    }