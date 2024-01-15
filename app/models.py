# models.py
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from backend import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name


class BaseImage(BaseModel):
    image = models.ImageField()
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class BlogImage(BaseImage):
    image = models.ImageField(upload_to="blogs/images/")
    name = models.CharField(max_length=255, default="blog_image")

    def __str__(self):
        return f"Blog Image - {str(self.id)}"


class Blog(BaseModel):
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


class Category(BaseModel):
    title = models.CharField(max_length=255)

    class Meta:
        managed = True
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class DestinationImage(BaseImage):
    image = models.ImageField(upload_to="destination/images/")
    name = models.CharField(max_length=255, default="destination_image")

    def __str__(self):
        return f"Destination Image - {str(self.id)}"


class Package(BaseModel):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    days = models.PositiveSmallIntegerField(default=5)
    night = models.PositiveSmallIntegerField(default=5)
    min_age = models.PositiveSmallIntegerField(default=10)
    people_max_limit = models.PositiveSmallIntegerField(default=10)
    pickup_location = models.CharField(max_length=50)
    drop_of_location = models.CharField(max_length=50)
    map_embed_link = models.TextField()
    image_list = models.ManyToManyField(PackageImage)
    price_quad_sharing = models.IntegerField(default=0)
    price_triple_sharing = models.IntegerField(default=0)
    price_double_sharing = models.IntegerField(default=0)
    price = models.IntegerField(default=0)  # Solo or starting From
    rating = models.PositiveSmallIntegerField(default=5)
    card_cover_image = models.ImageField(
        upload_to="package/covers/",
        default="static/images/trending/trending15.jpg",
        help_text="Image size should be 700 X 460. Click <a href='https://www.iloveimg.com/resize-image' style='color:lightblue'>here</a> to resize an image.",
    )

    def __str__(self) -> str:
        return self.name

    @property
    def rating_details(self):
        rating_list = [True] * self.rating + ([False] * (5 - self.rating))
        return rating_list


class Destination(BaseModel):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="India")
    rating = models.PositiveSmallIntegerField(default=5)
    description = RichTextField()
    image_list = models.ManyToManyField(DestinationImage)
    packages = models.ManyToManyField(Package, blank=True)
    map_embed_link = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self) -> str:
        return self.name


class Booking(BaseModel):
    STATUS_PENDING = "pending"
    STATUS_COMPLETED = "completed"
    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_COMPLETED, "Completed"),
    )

    package = models.ForeignKey(
        Package, on_delete=models.SET_NULL, blank=True, null=True
    )
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    total_adults = models.SmallIntegerField(default=0)
    total_childrens = models.SmallIntegerField(default=0)
    message = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING
    )


class KeyPoint(BaseModel):
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
        return f"Inclusive Note: {self.note}"


class Exclusive(KeyPoint):
    def __str__(self) -> str:
        return f"Exclusive Note: {self.note}"


class CarryThing(KeyPoint):
    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name="carry_things",
    )

    def __str__(self) -> str:
        return self.note


class Iternary(BaseModel):
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


# Signals


@receiver(post_save, sender=Booking)
def send_email_booking_to_admin(sender, instance, created, **kwargs):
    from django.contrib.auth import get_user_model

    User = get_user_model()

    get_admin_users = list(User.objects.all().values_list("email", flat=True))

    if created:
        subject = "New Booking from {instance.name}"
        message = f"A new {sender.__name__} has been submitted.\n\nDetails:\n{instance}"

        from_email = settings.EMAIL_HOST_USER  # Replace with your actual email address
        admin_emails = get_admin_users  # Replace with your admin's email address

        send_mail(subject, message, from_email, admin_emails)


@receiver(post_save, sender=Contact)
def send_email_to_admin(sender, instance, created, **kwargs):
    from django.contrib.auth import get_user_model

    User = get_user_model()

    get_admin_users = list(User.objects.all().values_list("email", flat=True))

    if created:
        subject = "Contact Query From {instance.name}"
        message = f"A new contact query has been submitted.\n\nDetails:\n{instance}\nPhone: {instance.phone}\nMessage: {instance.message}"

        from_email = settings.EMAIL_HOST_USER  # Replace with your actual email address
        admin_emails = get_admin_users  # Replace with your admin's email address

        send_mail(subject, message, from_email, admin_emails)
