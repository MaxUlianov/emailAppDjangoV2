from django import forms
# from email_sender_app.tasks import send_email


class EmailDataForm(forms.Form):
    address = forms.EmailField(label="Email Address")
    email_text = forms.CharField(
        label="Email Text", widget=forms.Textarea(attrs={"rows": 5})
    )

    def send_email(self):
        pass
