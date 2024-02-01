from django import forms
from custom_admin.models import CustomUser
from app.models import (
    Package,
    PackageImage,
    Category,
    Iternary,
    Inclusive,
    Exclusive,
    Booking,
)
from ckeditor.fields import RichTextField, RichTextFormField
from ckeditor.widgets import CKEditorWidget


class CustomUserAuthForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter Email"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Password",
                "class": "pass-input",
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ["email", "password"]


class BookingForm(forms.ModelForm):
    name = forms.CharField(
        label="name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Name",
            }
        ),
    )

    email = forms.EmailField(
        label="email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Email",
            }
        ),
    )
    phone = forms.CharField(
        label="phone",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Contact Number",
            }
        ),
    )

    total_adults = forms.IntegerField(
        min_value=1,
        label="No Of Adults",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "No Of Adults",
            }
        ),
    )

    total_childrens = forms.IntegerField(
        min_value=0,
        label="No Of Children",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "No Of Children",
            }
        ),
    )

    message = forms.CharField(
        label="message",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Message",
            }
        ),
    )

    # package = models.ForeignKey(
    #     Package, on_delete=models.SET_NULL, blank=True, null=True
    # )
    # email = models.EmailField(max_length=254)
    # phone = models.CharField(max_length=10)
    # name = models.CharField(max_length=255)
    # total_adults = models.SmallIntegerField(default=0)
    # total_childrens = models.SmallIntegerField(default=0)
    # message = models.TextField(blank=True)
    # status = models.CharField(
    #     max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING
    # )
    class Meta:
        model = Booking
        exclude = ["status"]


class InclusiveForm(forms.ModelForm):
    note = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Inclusive Note"}
        )
    )

    class Meta:
        model = Inclusive
        fields = "__all__"


InclusiveFormSet = forms.inlineformset_factory(
    parent_model=Package, model=Inclusive, form=InclusiveForm, min_num=1, extra=0
)


class ExclusiveForm(forms.ModelForm):
    note = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Exclusive Note"}
        )
    )

    class Meta:
        model = Exclusive
        fields = "__all__"


ExclusiveFormSet = forms.inlineformset_factory(
    parent_model=Package, model=Exclusive, form=ExclusiveForm, min_num=1, extra=0
)


class IternaryForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Iternary Title"}
        )
    )
    details = RichTextFormField()

    class Meta:
        model = Iternary
        fields = "__all__"


IternaryFormSet = forms.inlineformset_factory(
    parent_model=Package, model=Iternary, form=IternaryForm, min_num=1, extra=0
)


class ImagePreviewWidget(forms.widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super().render(name, value, attrs=None, **kwargs)
        if value:
            img_html = mark_safe(f'<br><br><img src="{value.url}" width="200" />')
            return f"{input_html}{img_html}"
        return input_html


class PackageForm(forms.ModelForm):
    name = forms.CharField(
        label="Package Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your package name",
            }
        ),
    )

    location = forms.CharField(
        label="Package Location",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Package location",
            }
        ),
    )

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "category-checkbox-row"}
            # attrs={"class": "form-control", "placeholder": "Enter Map Link"}
        ),
    )

    map_embed_link = forms.URLField(
        label="Map Link",
        widget=forms.URLInput(
            attrs={"class": "form-control", "placeholder": "Enter Map Link"}
        ),
    )

    description = forms.CharField(
        label="Description", widget=CKEditorWidget(config_name="default")
    )

    days = forms.IntegerField(
        label="Total Days",
        min_value=1,
        initial=5,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter Total No. of Days"}
        ),
    )

    night = forms.IntegerField(
        label="Total Nights",
        min_value=1,
        initial=5,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter Total No. of Nights"}
        ),
    )

    pickup_location = forms.CharField(
        label="Pickup Location",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Pickup Location"}
        ),
    )

    drop_of_location = forms.CharField(
        label="Drop Location",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Drop Location"}
        ),
    )

    min_age = forms.IntegerField(
        label="Min Age",
        min_value=1,
        max_value=150,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Minimum Age",
            }
        ),
    )

    people_max_limit = forms.IntegerField(
        label="Max People",
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Max People Limit",
            }
        ),
    )

    price = forms.IntegerField(
        label="Package Price",
        min_value=1,
        max_value=3000000,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Package Starting Price",
            }
        ),
    )

    price = forms.IntegerField(
        label="Package Price",
        min_value=1,
        max_value=3000000,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Package Starting Price",
            }
        ),
    )

    discount = forms.IntegerField(
        label="Discount",
        min_value=0,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Discount (in %)",
            }
        ),
    )

    rating = forms.IntegerField(
        label="Rating",
        min_value=1,
        initial=5,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Package Rating (1-5)",
            }
        ),
    )

    package_price_quad_sharing = forms.IntegerField(
        label="Quad Sharing",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter quad sharing price"}
        ),
    )

    price_quad_sharing = forms.IntegerField(
        label="Quad Sharing",
        min_value=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter Quad sharing price"}
        ),
    )

    price_triple_sharing = forms.IntegerField(
        min_value=0,
        label="Triple Sharing",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter Triple sharing price"}
        ),
    )

    price_double_sharing = forms.IntegerField(
        label="Double Sharing",
        min_value=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter Double sharing price"}
        ),
    )

    card_cover_image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "onchange": "loadFile(event)",
            }
        )
    )

    class Meta:
        model = Package
        fields = "__all__"


from django.utils.safestring import mark_safe


# class PackageForm(forms.ModelForm):
#     name = forms.CharField(max_length=50)
#     location = forms.CharField(max_length=50)
#     description = forms.TimeField(widget=CKEditorWidget())
#     # category = forms.ManyToManyField(Category)
#     # days = forms.PositiveSmallIntegerField(default=5)
#     # night = forms.PositiveSmallIntegerField(default=5)
#     # min_age = forms.PositiveSmallIntegerField(default=10)
#     # people_max_limit = forms.PositiveSmallIntegerField(default=10)
#     pickup_location = forms.CharField(max_length=50)
#     drop_of_location = forms.CharField(max_length=50)
#     map_embed_link = forms.URLField(widget=forms.URLInput())
#     # image_list = forms.ManyToManyField(PackageImage) #--
#     price_quad_sharing = forms.IntegerField(initial=0)
#     price_triple_sharing = forms.IntegerField(initial=0)
#     price_double_sharing = forms.IntegerField(initial=0)
#     price = forms.IntegerField(initial=0)  # Solo or starting From
#     rating = forms.IntegerField(initial=5)
#     discount = forms.IntegerField()

#     class Meta:
#         model = Package
#         fields = "__all__"
