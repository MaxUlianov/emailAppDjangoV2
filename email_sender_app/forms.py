from django import forms
from email_sender_app.tasks import send_email_task


class EmailDataForm(forms.Form):
    address = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={
        "placeholder": "Enter email address",
        "class": "input is-primary"
        })
    )
    subject = forms.CharField(
        label="Email Text", widget=forms.Textarea(attrs={
            "placeholder": "Email subject",
            "class": "input is-primary"
        })
    )
    email_text = forms.CharField(
        label="Email Text", widget=forms.Textarea(attrs={
            "rows": 5,
            "placeholder": "Enter email text",
            "class": "textarea is-primary is-normal"
        })
    )

    def send_email(self):
        send_email_task.delay(recipients=self.cleaned_data["address"],
                              text_message=self.cleaned_data["email_text"])


class EmailHTMLDataForm(EmailDataForm):
    html_text = forms.CharField(
        label="HTML Contents", widget=forms.Textarea(attrs={
            "rows": 5,
            "placeholder": "Enter html contents",
            "class": "textarea is-primary is-normal"
        })
    )


class PreviewHTMLForm(forms.Form):
    html = forms.CharField(
        label="HTML Text", widget=forms.Textarea(attrs={
            "rows": 10,
            "placeholder": "Enter your HTML here to preview",
            "class": "textarea is-primary is-normal"
        })
    )
