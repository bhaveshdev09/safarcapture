from django import forms
from app.models import Package, Blog
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget


class ContactForm(forms.Form):

    # name = forms.RegexField(strip=True, min_length=2, max_length=20, regex="^[A-Za-z]+(?:\s[A-Za-z]+)?(?:\s[A-Za-z]+)?$")
    name = forms.CharField(
        label="Your Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Name"}
        ),
        required=True,
    )

    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter Email"}
        ),
        required=True,
    )

    phone = forms.CharField(
        label="Your Phone Number",
        max_length=15,  # Adjust the max length as needed
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Mobile Number"}
        ),
        required=True,
    )

    message = forms.CharField(
        label="Your Message",
        widget=forms.Textarea(
            attrs={
                "rows": 4,
                "placeholder": "Enter a message",
                "name": "comments",
            }
        ),
        required=True,
    )


class BlogForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        fields = "__all__"
