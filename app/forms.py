from django import forms
from app.models import Package, Blog, Query, Destination
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


class DestinationQueryForm(forms.ModelForm):
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

    phone = forms.RegexField(
        label="Your Phone Number",
        strip=True,
        error_messages={"invalid": "Enter a valid mobile number."},
        regex=r"^[56789]\d{9}$",
        max_length=10,  # Adjust the max length as needed
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Mobile No.",
                "type": "tel",
                "pattern": "^[6789]\d{9}$",
            }
        ),
        required=True,
    )

    destination = forms.ModelChoiceField(
        queryset=Destination.objects.all(),
        empty_label="Select Destination",
        widget=forms.Select(attrs={"class": "niceSelect", "required": True}),
        required=True,
    )

    total_adults = forms.IntegerField(
        initial=1,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Adults"}
        ),
        required=True,
    )

    total_childrens = forms.IntegerField(
        initial=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Children"}
        ),
        required=True,
    )

    status = forms.ChoiceField(
        choices=Query.FOLLOWUP_STATUS_CHOICES,
        initial=Query.FOLLOWUP_STATUS_PENDING,
        required=False,
    )

    class Meta:
        model = Query
        fields = "__all__"


class BlogForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        fields = "__all__"
