from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DetailView
from app.forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
from app.models import Contact, Blog, Package, Destination, Booking


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


class BlogListView(ListView):
    model = Blog
    template_name = "blogs.html"
    context_object_name = "blogs"
    paginate_by = 4

    def get_queryset(self):
        order_by = self.request.GET.get("order_by", "asc")
        if order_by == "desc":
            return Blog.objects.all().order_by("-published_date")
        else:
            return Blog.objects.all().order_by("published_date")


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"
    context_object_name = "blog"


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("success")  # You need to define this URL

    def form_valid(self, form):
        contact = Contact(
            name=form.cleaned_data["name"],
            email=form.cleaned_data["email"],
            phone=form.cleaned_data["phone"],
            message=form.cleaned_data["message"],
        )
        contact.save()
        # Optionally, you can add a success message
        # messages.success(self.request, "Your message has been sent successfully!")

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "There was an error with your submission. Please check the form.",
        )
        return super().form_invalid(form)


class PackageDetailView(DetailView):
    model = Package
    template_name = "package_detail.html"
    context_object_name = "package"

    def get_queryset(self):
        return Package.objects.prefetch_related("image_list").all() 


class DestinationDetailView(DetailView):
    model = Destination
    template_name = "destination_detail.html"
    context_object_name = "destination"

    def get_queryset(self):
        return Destination.objects.prefetch_related("image_list").all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        destination_object = context.get("object")
        destination_object.rating_details = [True] * destination_object.rating + (
            [False] * (5 - destination_object.rating)
        )
        print(destination_object.rating_details)
        return context


# class PackageBookingView(DetailView):
#     model = Booking
#     template_name = "destination_detail.html"
#     context_object_name = "destination"

#     def get_queryset(self):
#         return Destination.objects.prefetch_related("image_list").all()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         destination_object = context.get("object")
#         destination_object.rating_details = [True] * destination_object.rating + (
#             [False] * (5 - destination_object.rating)
#         )
#         print(destination_object.rating_details)
#         return context


def post_booking(request):
    if request.method == "POST":
        print(request.POST)
        return redirect("index")


def faq(request):
    return render(request, "faq.html")


def success(request):
    return render(request, "success.html")
