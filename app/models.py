# models.py
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name


class BaseImage(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class BlogImage(BaseImage):
    image = models.ImageField(upload_to="blogs/images/")
    name = models.CharField(max_length=255, default="blog_image")

    def __str__(self):
        return f"Blog Image - {str(self.id)}"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    cover_image = models.ImageField(upload_to="blogs/covers/")
    image_list = models.ManyToManyField(BlogImage)
    published_date = models.DateField(default=timezone.now)
    quote = models.TextField()
    author = models.CharField(
        max_length=255
    )  # TODO: convert this field to Foreignkey to user
    # rating = models.PositiveSmallIntegerField()  # TODO: Not Integrated Yet in template

    def __str__(self):
        return self.title


class PackageImage(BaseImage):
    image = models.ImageField(upload_to="package/images/")
    name = models.CharField(max_length=255, default="package_image")

    def __str__(self):
        return f"Package Image - {str(self.id)}"


class Package(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField()
    days = models.PositiveSmallIntegerField(default=5)
    night = models.PositiveSmallIntegerField(default=5)
    people_max_limit = models.PositiveSmallIntegerField(default=10)
    pickup_location = models.CharField(max_length=50)
    drop_of_location = models.CharField(max_length=50)
    map_embed_link = models.TextField()
    image_list = models.ManyToManyField(BlogImage)
    price_quad_sharing = models.IntegerField(default=0)
    price_triple_sharing = models.IntegerField(default=0)
    price_double_sharing = models.IntegerField(default=0)
    rating = models.PositiveSmallIntegerField(default=5)

    def __str__(self) -> str:
        return self.name


class KeyPoint(models.Model):
    note = models.TextField()
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, default=None, null=True, blank=True
    )

    class Meta:
        abstract = True


class Inclusive(KeyPoint):
    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name="inclusives",
    )

    def __str__(self) -> str:
        return f"Inclusive Note: {self.id}"


class Exclusive(KeyPoint):
    def __str__(self) -> str:
        return f"Exclusive Note: {self.id}"


class Iternary(models.Model):
    title = models.CharField(max_length=255)
    details = RichTextField(blank=True, null=True, default="--empty--")
    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name="iternaries",
    )

    # price_includes = models.JSONField()
    # price_excludes = models.JSONField()
    # price_quad_sharing = models.IntegerField()
    # price_triple_sharing = models.IntegerField()
    # price_double_sharing = models.IntegerField()
    # iternary = models.JSONField(null=True)
    # costing = models.JSONField(null=True)
    # images = models.ManyToManyField(PackageImage)
    # rating = models.IntegerField(
    #     validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True
    # )
