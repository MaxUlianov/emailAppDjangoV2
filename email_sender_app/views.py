from django.shortcuts import render
from email_sender_app.forms import EmailDataForm, EmailHTMLDataForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


class EmailDataFormView(FormView):
    template_name = 'email_input.html'
    form_class = EmailDataForm
    success_url = '/email_sender/email_sender_success/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class EmailHTMLDataFormView(EmailDataFormView):
    template_name = 'email_html_input.html'
    form_class = EmailHTMLDataForm


class EmailSendSuccess(TemplateView):
    template_name = 'email_send_success.html'


def preview_email(request, html_email):
    return render(request, html_email)
