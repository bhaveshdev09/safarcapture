from django.contrib import admin
from django.utils.html import format_html
from app.models import (
    Blog,
    BlogImage,
    Exclusive,
    Inclusive,
    Package,
    Iternary,
    Contact,
)
from django.db import models
from django import forms


class BlogImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="75px"/>'.format(obj.image.url))

    image_tag.short_description = "Image"
    list_display = [
        "image_tag",
    ]


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_date"]


class InclusiveInline(admin.StackedInline):
    model = Inclusive
    extra = 0
    min_num = 3

    formfield_overrides = {
        models.TextField: {"widget": forms.Textarea(attrs={"rows": 2, "cols": 150})},
    }


class ExclusiveInline(admin.StackedInline):
    model = Exclusive
    extra = 0
    min_num = 3

    formfield_overrides = {
        models.TextField: {"widget": forms.Textarea(attrs={"rows": 2, "cols": 150})},
    }


class IternaryInline(admin.StackedInline):
    model = Iternary
    extra = 0
    min_num = 2


class PackageAdmin(admin.ModelAdmin):
    inlines = [InclusiveInline, ExclusiveInline, IternaryInline]

    formfield_overrides = {
        models.TextField: {"widget": forms.Textarea(attrs={"rows": 4, "cols": 150})},
    }

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "name",
                    "location",
                    "description",
                    "map_embed_link",
                    ("pickup_location", "drop_of_location"),
                    ("days", "night", "people_max_limit", "rating"),
                ],
            },
        ),
        (
            "People Sharing Cost",
            {
                "fields": [
                    (
                        "price_quad_sharing",
                        "price_triple_sharing",
                        "price_double_sharing",
                    ),
                ]
            },
        ),
        (
            "Images",
            {
                # "classes": ["collapse"],
                "fields": ["image_list"],
            },
        ),
    ]


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogImage, BlogImageAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Contact)
