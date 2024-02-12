from django.contrib import admin
from django.utils.html import format_html
from app.models import (
    Blog,
    BlogImage,
    Exclusive,
    Inclusive,
    PackageImage,
    Package,
    Iternary,
    Contact,
    CarryThing,
    Category,
    Destination,
    DestinationImage,
    Booking,
    Query,
    GalleryImage,
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


class PackageImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="75px"/>'.format(obj.image.url))

    image_tag.short_description = "Image"
    list_display = [
        "image_tag",
    ]


class DestinationImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="75px"/>'.format(obj.image.url))

    image_tag.short_description = "Image"
    list_display = [
        "image_tag",
    ]


class QueryAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "message", "destination"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_date"]


class InclusiveInline(admin.StackedInline):
    model = Inclusive
    extra = 0
    min_num = 2

    formfield_overrides = {
        models.TextField: {"widget": forms.Textarea(attrs={"rows": 2, "cols": 150})},
    }


class ExclusiveInline(admin.StackedInline):
    model = Exclusive
    extra = 0
    min_num = 2

    formfield_overrides = {
        models.TextField: {"widget": forms.Textarea(attrs={"rows": 2, "cols": 150})},
    }


class CarryThingInline(admin.TabularInline):
    model = CarryThing
    extra = 0
    min_num = 0

    formfield_overrides = {
        models.TextField: {"widget": forms.Textarea(attrs={"rows": 2, "cols": 150})},
    }


class IternaryInline(admin.StackedInline):
    model = Iternary
    extra = 0
    min_num = 1


class DestinationAdmin(admin.ModelAdmin):

    filter_horizontal = ("image_list",)


class PackageAdmin(admin.ModelAdmin):
    inlines = [InclusiveInline, ExclusiveInline, IternaryInline, CarryThingInline]

    formfield_overrides = {
        models.TextField: {"widget": forms.Textarea(attrs={"rows": 4, "cols": 150})},
    }

    filter_horizontal = (
        "category",
        "image_list",
    )

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "name",
                    "location",
                    "category",
                    "description",
                    "map_embed_link",
                    ("pickup_location", "drop_of_location"),
                    ("days", "night"),
                    ("people_max_limit", "min_age", "rating"),
                ],
            },
        ),
        (
            "People Sharing Cost",
            {
                "fields": [
                    ("discount", "price"),
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
                "fields": ["card_cover_image", "image_list"],
            },
        ),
    ]


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogImage, BlogImageAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(PackageImage, PackageImageAdmin)
admin.site.register(Contact)
admin.site.register(Category, CategoryAdmin)
admin.site.register(DestinationImage, DestinationImageAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Booking)
admin.site.register(Query, QueryAdmin)
admin.site.register(GalleryImage)
