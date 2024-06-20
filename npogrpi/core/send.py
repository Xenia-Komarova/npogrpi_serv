from django.core.mail import send_mail
from npogrpi.settings import EMAIL_HOST_USER


def send_email_to_admin(form_data):
    subject = 'Новый запрос на поиск продукции'
    message = f'Новый запрос на поиск продукции:\n\n'
    for key, value in form_data.items():
        message += f'{key}: {value}\n'
    sender = EMAIL_HOST_USER
    recipients = ['komarova@npp-in.ru']  # Замените на реальный email администратора
    send_mail(subject, message, sender, recipients)
