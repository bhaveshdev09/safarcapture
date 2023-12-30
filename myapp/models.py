from django.db import models

class PackageImage(models.Model):
    image = models.ImageField(upload_to='packages/')    
    def __str__(self) -> str:
        return f"{self.image.name}"

class DestinationImage(models.Model):
    image = models.ImageField(upload_to='destinations/')

class Destination(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    images = models.ManyToManyField(DestinationImage)
    map_link = models.URLField() # -- URL
    

class Package(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    iternary = models.JSONField()
    costing = models.JSONField()
    inclusion = models.JSONField()
    exclude = models.JSONField()
    images = models.ManyToManyField(PackageImage)

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