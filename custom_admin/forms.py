from django import forms
from custom_admin.models import CustomUser


class CustomUserAuthForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email address"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password",
                "class": "pass-input",
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ["email", "password"]
