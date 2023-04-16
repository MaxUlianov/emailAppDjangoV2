from django.urls import path
from email_sender_app.views import EmailDataFormView, EmailSendSuccess, EmailHTMLDataFormView,\
    PreviewHTMLFormView, LoginView, LoginFormView

app_name = "email_sender_app"

urlpatterns = [
    path('email_sender/', EmailDataFormView.as_view(), name='email_form'),
    path('email_sender/email_html/', EmailHTMLDataFormView.as_view(), name='email_html_form'),
    path('email_sender/email_sender_success/', EmailSendSuccess.as_view(), name='email_send_success'),
    path('email_sender/preview_html/', PreviewHTMLFormView.as_view(), name='preview_html'),
    # path('email_sender/preview_html_view', )
    path('email_sender/login_status', LoginView.as_view(), name='login_status'),
    path('email_sender/login_form', LoginFormView.as_view(), name='login_form')
]
