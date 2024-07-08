from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Ваше имя'), max_length=100)
    company = forms.CharField(label=_('Ваша компания'), max_length=100)
    telephone = forms.CharField(label=_('Ваш телефон'), max_length=11)
    email = forms.EmailField(label=_('Ваш Email'), max_length=100)
    message = forms.CharField(label=_('Ваше сообщение'), widget=forms.Textarea)