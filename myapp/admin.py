from django.contrib import admin
from django.utils.html import format_html
from .models import *


class PackageAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
admin.site.register(Package, PackageAdmin)


class PackageImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="50px"/>'.format(obj.image.url))
    image_tag.short_description = 'Image'
    list_display = ['image_tag',]
admin.site.register(PackageImage, PackageImageAdmin)

class QueryFormAdmin(admin.ModelAdmin):
    list_display = ["id", "email","full_name", "destination"]
admin.site.register(Query, QueryFormAdmin)

class DestinationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "state", "description"]
admin.site.register(Destination, DestinationAdmin)


class DestinationImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="50px"/>'.format(obj.image.url))
    image_tag.short_description = 'Image'
    list_display = ['image_tag',]
admin.site.register(DestinationImage,DestinationImageAdmin)