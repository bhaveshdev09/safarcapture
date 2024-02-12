from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    FormView,
    ListView,
    TemplateView,
    CreateView,
)

from app.forms import ContactForm, DestinationQueryForm
from app.models import (
    Blog,
    Booking,
    Category,
    Contact,
    Destination,
    Package,
    GallaryImage,
)
from custom_admin.forms import BookingForm


class IndexView(FormView):
    template_name = "index.html"
    form_class = DestinationQueryForm
    success_url = reverse_lazy("success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        destinations = Destination.objects.all()
        categories = Category.aggrgate_categories()
        packages = Package.objects.all().order_by("price")
        blogs = Blog.objects.all()[:4]
        master_blog = Blog.objects.all().order_by("-created_at").first()
        special_offers = packages.filter(discount__gte=1)
        packages = packages[:6]

        context.update(
            {
                "destinations": destinations,
                "categories": categories,
                "packages": packages,
                "blogs": blogs,
                "master_blog": master_blog,
                "special_offers": special_offers,
            }
        )

        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(
            self.request,
            "There was an error with your submission. Please check the form.",
        )
        return super().form_invalid(form)


class AboutView(TemplateView):
    template_name = "about.html"


class TermsConditionView(TemplateView):
    template_name = "terms_conditions.html"


class PrivacyPolicyView(TemplateView):
    template_name = "privacy_policy.html"


class GalleryView(ListView):
    template_name = "gallery.html"
    context_object_name = "images"
    paginate_by = 8
    model = GallaryImage
    queryset = GallaryImage.objects.all().order_by("-created_at")


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["booking_form"] = BookingForm
        return context

    def get_queryset(self):
        return Package.objects.prefetch_related("image_list").all()


class DestinationDetailView(DetailView):
    model = Destination
    template_name = "destination_detail.html"
    context_object_name = "destination"

    def get_queryset(self):
        return Destination.objects.prefetch_related("image_list").all()


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


class BookingView(FormView):
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

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "There was an error with your submission. Please check the form.",
        )
        return super().form_invalid(form)


def post_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save(commit=True)
        return redirect("index")


class FAQView(TemplateView):
    template_name = "faq.html"


class SuccessView(TemplateView):
    template_name = "success.html"
