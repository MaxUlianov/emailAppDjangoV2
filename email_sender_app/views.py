import logging

from django.shortcuts import render, redirect
from email_sender_app.forms import EmailDataForm, EmailHTMLDataForm, PreviewHTMLForm, LoginForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView, View
from django.utils.html import format_html

from .sender_credentials import write_user_credentials, user_credentials_available,\
    read_user_credentials, erase_user_credentials


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


class LoginView(View):
    def get(self, request):
        if user_credentials_available():
            # Render login_status
            data = read_user_credentials()
            return render(request, 'login_status.html', {
                'email': data['email'],
                'host': data['host'],
                'port': data['port']
            })
        else:
            # Redirect to LoginForm
            return redirect('email_sender_app:login_form')

    def post(self, request):
        # Delete creds, redirect to LoginForm
        erase_user_credentials()
        return redirect('email_sender_app:login_form')


class LoginFormView(View):
    def get(self, request):
        # Render LoginForm
        form = LoginForm()
        return render(request, 'login_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            host = form.cleaned_data['host']
            port = form.cleaned_data['port']

            write_user_credentials(email, password, host, port)

            # Redirect to login_status
            return redirect('email_sender_app:login_status')
        else:
            # Re-render LoginForm
            return render(request, 'login_form.html', {'form': form})
