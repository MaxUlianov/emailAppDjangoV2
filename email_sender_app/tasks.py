import logging

from celery import shared_task
from django.core.mail import send_mail
from django.core.mail.backends.smtp import EmailBackend
from django.utils.html import strip_tags
from email_project_v2.settings import DEFAULT_FROM_EMAIL
from sender_credentials import user_credentials_available, read_user_credentials


@shared_task
def send_email_task(recipients, subject="", email_text=None, html_text=None, sender_address=DEFAULT_FROM_EMAIL):
    if html_text and not email_text:
        email_text = strip_tags(html_text)

    try:
        if user_credentials_available():
            email_creds = read_user_credentials()

            custom_connection = EmailBackend(
                host=email_creds['host'],
                port=email_creds['port'],
                username=email_creds['email'],
                password=email_creds['password']
            )

            send_mail(subject=subject,
                      recipient_list=[recipients],
                      from_email=email_creds['email'],
                      message=email_text,
                      html_message=html_text,
                      connection=custom_connection)
        else:
            send_mail(subject=subject,
                      recipient_list=[recipients],
                      from_email=sender_address,
                      message=email_text,
                      html_message=html_text)
    except Exception as e:
        logging.error(repr(e))
