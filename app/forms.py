from django import forms


class ContactForm(forms.Form):
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
            attrs={"class": "form-control", "placeholder": "Eter Mobile Number"}
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

    # def clean_name(self):
    #     name = self.cleaned_data.get("name")
    #     if len(name.split()) < 2:
    #         raise forms.ValidationError("Please enter your full name.")
    #     return name

    # def clean_message(self):
    #     message = self.cleaned_data.get("message")
    #     if len(message) < 10:
    #         raise forms.ValidationError(
    #             "Your message should be at least 10 characters long."
    #         )
    #     return message
