from django.contrib import admin
from django.utils.html import format_html
from .models import *



class PackageAdmin(admin.ModelAdmin):
    list_display = ["id", "name","location","days","night","pickup_location","dropof_location","iternary","costing"]
admin.site.register(Package, PackageAdmin)


class PackageImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="50px"/>'.format(obj.image.url))
    image_tag.short_description = 'Image'
    list_display = ['image_tag',]
admin.site.register(PackageImage, PackageImageAdmin)

class QueryAdmin(admin.ModelAdmin):
    list_display = ["id", "email","full_name", "destination"]
admin.site.register(Query, QueryAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "fname","lname", "phone_number","message","updated_at","is_contacted","admin_remark"]
admin.site.register(Contact, ContactAdmin)

class DestinationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "state", "description"]
admin.site.register(Destination, DestinationAdmin)

class DestinationImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="50px"/>'.format(obj.image.url))
    image_tag.short_description = 'Image'
    list_display = ['image_tag',]
admin.site.register(DestinationImage,DestinationImageAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ["booking_id", "is_confirmed","is_paid","full_name","phone_number","adult_count","child_count","message"]
admin.site.register(Booking,BookingAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id","seen" ,"name", "updated_at", "message","admin_remark"]
admin.site.register(Review, ReviewAdmin)


