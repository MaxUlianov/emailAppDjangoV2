from django import forms
from email_sender_app.tasks import send_email_task


LINE_INPUT_FIELD_CLASS = "input is-primary"
TEXTAREA_FIELD_CLASS = "textarea is-primary is-normal"


class EmailDataForm(forms.Form):
    address = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={
        "placeholder": "Enter email address",
        "class": LINE_INPUT_FIELD_CLASS
        })
    )
    subject = forms.CharField(
        label="Email Text", widget=forms.Textarea(attrs={
            "placeholder": "Email subject",
            "class": LINE_INPUT_FIELD_CLASS
        }), required=False
    )
    email_text = forms.CharField(
        label="Email Text", widget=forms.Textarea(attrs={
            "rows": 5,
            "placeholder": "Enter email text",
            "class": TEXTAREA_FIELD_CLASS
        })
    )

    def send_email(self):
        send_email_task.delay(
            recipients=self.address,
            subject=self.subject,
            email_text=self.email_text,
        )


class EmailHTMLDataForm(EmailDataForm):
    email_text = forms.CharField(
        label="Email Text", widget=forms.Textarea(attrs={
            "rows": 5,
            "placeholder": "Enter email text",
            "class": TEXTAREA_FIELD_CLASS
        }), required=False
    )
    html_text = forms.CharField(
        label="HTML Contents", widget=forms.Textarea(attrs={
            "rows": 5,
            "placeholder": "Enter html contents",
            "class": TEXTAREA_FIELD_CLASS
        })
    )

    def send_email(self):
        send_email_task.delay(
            recipients=self.address,
            subject=self.subject,
            email_text=self.email_text,
            html_text=self.html_text
        )


class PreviewHTMLForm(forms.Form):
    html = forms.CharField(
        label="HTML Text", widget=forms.Textarea(attrs={
            "rows": 10,
            "placeholder": "Enter your HTML here to preview",
            "class": TEXTAREA_FIELD_CLASS
        })
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="User Email Address", widget=forms.EmailInput(attrs={
            "placeholder": "Email address",
            "class": LINE_INPUT_FIELD_CLASS
        })
    )
    password = forms.CharField(
        label="User Email Password", widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": LINE_INPUT_FIELD_CLASS
        })
    )
    host = forms.CharField(
        label="User Email host (provider)", widget=forms.TextInput(attrs={
            "placeholder": "Email provider",
            "class": LINE_INPUT_FIELD_CLASS
        })
    )
    port = forms.RegexField(
        label="Email Host Port", widget=forms.TextInput(attrs={
            "placeholder": "Email host (provider)",
            "class": LINE_INPUT_FIELD_CLASS
        }),
        regex="^(\d+)$"
    )
