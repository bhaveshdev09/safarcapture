from django.contrib import admin
from django.utils.html import format_html
from app.models import Blog, BlogImage


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


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogImage, BlogImageAdmin)
