from django.urls import path
from email_sender_app.views import EmailDataFormView, EmailSendSuccess, EmailHTMLDataFormView, preview_email

app_name = "email_sender_app"

urlpatterns = [
    path('email_sender/', EmailDataFormView.as_view(), name='email_form'),
    path('email_sender/email_html/', EmailHTMLDataFormView.as_view(), name='email_html_form'),
    path('email_sender/view_html/', preview_email),
    path('email_sender/email_sender_success/', EmailSendSuccess.as_view(), name='email_send_success')
]
