from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    company = forms.CharField(label='Ваша компания', max_length=100)
    telephone = forms.CharField(label='Ваш телефон', max_length=11)
    email = forms.EmailField(label='Ваш Email', max_length=100)
    message = forms.CharField(label='Ваше сообщение', widget=forms.Textarea)