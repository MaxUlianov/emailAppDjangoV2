from celery import shared_task
from django.core.mail import send_mail
from email_project_v2.settings import DEFAULT_FROM_EMAIL


@shared_task
def send_email_task(recipients, text_message, subject="No Subject", sender_address=None):
    if sender_address:
        send_mail(subject=subject,
                  recipient_list=[recipients],
                  from_email=sender_address,
                  message=text_message
                  )
    else:
        send_mail(subject=subject,
                  recipient_list=[recipients],
                  from_email=DEFAULT_FROM_EMAIL,
                  message=text_message
                  )
