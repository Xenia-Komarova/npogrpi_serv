from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from npogrpi.settings import EMAIL_HOST_USER

from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            company = form.cleaned_data['company']
            telephone = form.cleaned_data['telephone']
            message = form.cleaned_data['message']
            subject = f'Сообщение от {name} ({email})'
            full_message = f'Компания: {company}\n\n{message}\n\nТелефон: {telephone}'
            send_mail(
                subject,
                full_message,
                EMAIL_HOST_USER,
                ['komarova@npp-in.ru'],  # Замените на адрес получателя
                fail_silently=False,
            )
            messages.success(request, 'Сообщение успешно отправлено')
            return redirect('website/contacts.html')  # Замените на шаблон, который показывается после успешной отправки
    else:
        form = ContactForm()
    return render(request, 'website/contacts.html', {'form': form})# Create your views here.

def page_not_found(request, exception):
    return render(request, 'core/404.html', {'path': request.path}, status=404)

def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html')

def server_error(request):
    return render(request, 'core/500.html', status=500)

def permission_denied(request, exception):
    return render(request, 'core/403.html', status=403)
