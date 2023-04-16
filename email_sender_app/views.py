import logging

from django.shortcuts import render, redirect
from email_sender_app.forms import EmailDataForm, EmailHTMLDataForm, PreviewHTMLForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils.html import format_html


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


class PreviewHTMLFormView(FormView):
    template_name = 'html_preview_form.html'
    form_class = PreviewHTMLForm
    success_url = '/email_sender/preview_html_view/'

    html_preview_template = 'html_preview_base.html'

    def form_valid(self, form):
        html = format_html(form.cleaned_data['html'])
        logging.info(f'cleaned html = {html}')
        return render(self.request, self.html_preview_template, {'html': html})

