# models.py
from django.db import models
from django.utils import timezone


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
    description = models.TextField()
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
