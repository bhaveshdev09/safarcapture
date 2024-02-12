# models.py
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from backend import settings
from PIL import Image
import os


class State(models.TextChoices):
    ANDHRA_PRADESH = "AP", "Andhra Pradesh"
    ARUNACHAL_PRADESH = "AR", "Arunachal Pradesh"
    ASSAM = "AS", "Assam"
    BIHAR = "BR", "Bihar"
    CHHATTISGARH = "CT", "Chhattisgarh"
    GOA = "GA", "Goa"
    GUJARAT = "GJ", "Gujarat"
    HARYANA = "HR", "Haryana"
    HIMACHAL_PRADESH = "HP", "Himachal Pradesh"
    JHARKHAND = "JH", "Jharkhand"
    KARNATAKA = "KA", "Karnataka"
    KERALA = "KL", "Kerala"
    MADHYA_PRADESH = "MP", "Madhya Pradesh"
    MAHARASHTRA = "MH", "Maharashtra"
    MANIPUR = "MN", "Manipur"
    MEGHALAYA = "ML", "Meghalaya"
    MIZORAM = "MZ", "Mizoram"
    NAGALAND = "NL", "Nagaland"
    ODISHA = "OR", "Odisha"
    PUNJAB = "PB", "Punjab"
    RAJASTHAN = "RJ", "Rajasthan"
    SIKKIM = "SK", "Sikkim"
    TAMIL_NADU = "TN", "Tamil Nadu"
    TELANGANA = "TG", "Telangana"
    TRIPURA = "TR", "Tripura"
    UTTAR_PRADESH = "UP", "Uttar Pradesh"
    UTTARAKHAND = "UK", "Uttarakhand"
    WEST_BENGAL = "WB", "West Bengal"


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
    # followup = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class BaseImage(BaseModel):
    image = models.ImageField()
    name = models.CharField(max_length=255, blank=True, default="")

    class Meta:
        abstract = True


class GallaryImage(BaseImage):
    image = models.ImageField(upload_to="gallery/images/")

    def __str__(self):
        return f"Gallery Image - {str(self.id)}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width != 700 or img.height != 460:
            output_size = (700, 460)
            resized_image = img.resize(output_size)
            resized_image.save(self.image.path)


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
    image = models.ImageField(
        upload_to="package/images/", default="package/images/bg.jpg"
    )
    name = models.CharField(max_length=255, default="package_image")

    def __str__(self):
        image_filename = os.path.basename(self.image.name)
        return f"Package Image - {str(self.id)} : {image_filename}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width != 1600 or img.height != 800:
            output_size = (1600, 800)
            resized_image = img.resize(output_size)
            resized_image.save(self.image.path)


class Category(BaseModel):
    title = models.CharField(max_length=255)

    class Meta:
        managed = True
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title

    @classmethod
    def aggrgate_categories(cls, count=1):
        return (
            cls.objects.all()
            .annotate(dest_count=models.Count("destination"))
            .filter(dest_count__gte=count)
        )


class DestinationImage(BaseImage):
    image = models.ImageField(upload_to="destination/images/")
    name = models.CharField(max_length=255, default="destination_image")

    def __str__(self):
        return f"Destination Image - {str(self.id)}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width != 1600 or img.height != 800:
            output_size = (1600, 800)
            resized_image = img.resize(output_size)
            resized_image.save(self.image.path)


class Package(BaseModel):

    name = models.CharField(max_length=50)
    location = models.CharField(
        max_length=50, choices=State.choices, default=State.UTTARAKHAND
    )
    description = RichTextField()
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
    discount = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(limit_value=100)]
    )
    card_cover_image = models.ImageField(
        upload_to="package/covers/",
        default="package/covers/bg.jpg",
        help_text="Image size should be 700 X 460.",
    )

    def __str__(self) -> str:
        return self.name

    def is_discount_available(self):
        return self.discount > 0

    def get_discounted_price(self):
        return int(round(self.price * (100 - self.discount) * 0.01, 0))

    @property
    def rating_details(self):
        rating_list = [True] * self.rating + ([False] * (5 - self.rating))
        return rating_list

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.card_cover_image.path)
        if img.width != 700 or img.height != 460:
            output_size = (700, 460)
            resized_image = img.resize(output_size)
            resized_image.save(self.card_cover_image.path)


class Destination(BaseModel):
    name = models.CharField(max_length=50)
    location = models.CharField(
        max_length=50, choices=State.choices, default=State.UTTARAKHAND
    )
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

    @property
    def rating_details(self):
        rating_list = [True] * self.rating + ([False] * (5 - self.rating))
        return rating_list


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


class Query(BaseModel):
    FOLLOWUP_STATUS_PENDING = "pending"
    FOLLOWUP_STATUS_COMPLETED = "completed"
    FOLLOWUP_STATUS_CHOICES = (
        (FOLLOWUP_STATUS_PENDING, "Pending"),
        (FOLLOWUP_STATUS_COMPLETED, "Completed"),
    )

    destination = models.ForeignKey(
        Destination, on_delete=models.SET_NULL, blank=True, null=True
    )
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    total_adults = models.SmallIntegerField(default=0)
    total_childrens = models.SmallIntegerField(default=0)
    message = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=FOLLOWUP_STATUS_CHOICES, default=FOLLOWUP_STATUS_PENDING
    )


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

    def __str__(self) -> str:
        return self.title

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
        subject = f"New Booking from {instance.name}"
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
        subject = f"Contact Query From {instance.name}"
        message = f"A new contact query has been submitted.\n\nDetails:\nName: {instance}\nEmail: {instance.email}\nPhone: {instance.phone}\nMessage: {instance.message}"

        from_email = settings.EMAIL_HOST_USER  # Replace with your actual email address
        admin_emails = get_admin_users  # Replace with your admin's email address

        send_mail(subject, message, from_email, admin_emails)


@receiver(post_save, sender=Query)
def send_email_destination_query_to_admin(sender, instance, created, **kwargs):
    from django.contrib.auth import get_user_model

    User = get_user_model()

    get_admin_users = list(User.objects.all().values_list("email", flat=True))

    if created:
        subject = f"Destination Query from {instance.name}"
        message = f"A new {sender.__name__} has been submitted.\n\nDetails:\nUser: {instance.name}\nPhone No: {instance.phone}\nDestination: {instance.destination}\nMessage: {instance.message}\n"

        from_email = settings.EMAIL_HOST_USER  # Replace with your actual email address
        admin_emails = get_admin_users  # Replace with your admin's email address

        send_mail(subject, message, from_email, admin_emails)
