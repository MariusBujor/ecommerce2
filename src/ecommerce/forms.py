from django import forms


class ContactForm(forms.Form):

    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Full Name"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email"
                }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Your Content"
                }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com , yahoo.com" in email:
            raise forms.ValidationError("Email has to be gmail.com or yahoo.com")
        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


        