from django.shortcuts import redirect
from django.utils.translation import get_language, activate, LANGUAGE_SESSION_KEY


def switch_lang(request):
    current_language = get_language()
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
        'current_language': current_language,
        'switch_lang_url': switch_lang_url,
    }