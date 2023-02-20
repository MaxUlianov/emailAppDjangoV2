from django import forms
# from email_sender_app.tasks import send_email


class EmailDataForm(forms.Form):
    address = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={
        "placeholder": "Enter email address",
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
        pass
