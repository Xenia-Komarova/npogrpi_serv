from django import template
from django.utils.translation import get_language
from core.models import MenuItem

register = template.Library()


@register.inclusion_tag('includes/menu.html', takes_context=True)
def show_menu(context):
    menu_items = MenuItem.objects.filter(level=1)
    
    for item in menu_items:
        if get_language() == 'en':
            item.display_name = item.name_en
        else:
            item.display_name = item.name
    return {
        'menu_items': menu_items,
    }