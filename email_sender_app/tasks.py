from celery import shared_task
from django.core.mail import send_mail
from django.utils.html import strip_tags
from email_project_v2.settings import DEFAULT_FROM_EMAIL


@shared_task
def send_email_task(recipients, subject="", email_text=None, html_text=None, sender_address=DEFAULT_FROM_EMAIL):
    if html_text and not email_text:
        email_text = strip_tags(html_text)

    send_mail(subject=subject,
              recipient_list=[recipients],
              from_email=sender_address,
              message=email_text,
              html_message=html_text)
