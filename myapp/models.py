from django.db import models

class PackageImage(models.Model):
    image = models.ImageField(upload_to='packages/')    
    def __str__(self) -> str:
        return f"{self.image.name}"

class DestinationImage(models.Model):
    image = models.ImageField(upload_to='destinations/')

class Destination(models.Model):
    name = models.CharField(max_length=50)
    destination_location = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    state = models.CharField(max_length=30, null=True)
    images = models.ManyToManyField(DestinationImage)
    map_link = models.URLField() # -- URL
    

class Package(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField()
    days = models.IntegerField()
    night = models.IntegerField()
    pickup_location = models.CharField(max_length=50)
    dropof_location = models.CharField(max_length=50)
    price_includes = models.JSONField()
    price_excludes = models.JSONField()
    price_quad_sharing = models.IntegerField()
    price_triple_sharing = models.IntegerField()
    price_double_sharing = models.IntegerField()
    iternary = models.JSONField(null=True)
    costing = models.JSONField(null=True)
    images = models.ManyToManyField(PackageImage)
    # slug = models.SlugField() -- TODO: this is to check
    

#customer package query table
class Query(models.Model):
    full_name = models.CharField(max_length=40)
    phone_number = models.IntegerField()
    email = models.EmailField()
    destination = models.TextField(max_length=100)
    adult_count = models.IntegerField()
    child_count = models.IntegerField()
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_contacted = models.BooleanField(default=False)
    admin_remark = models.TextField(max_length=200)

# customer contact query table
class Contact(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number = models.IntegerField()
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_contacted = models.BooleanField(default=False)
    admin_remark = models.TextField(max_length=200,blank=True, null=True)
    
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=40)
    phone_number = models.IntegerField()
    email = models.EmailField()
    adult_count = models.IntegerField()
    child_count = models.IntegerField()
    message = models.CharField(max_length=200)
    is_confirmed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

class Review(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seen = models.BooleanField(default=False)
    admin_remark = models.TextField(max_length=200,blank=True, null=True)
    