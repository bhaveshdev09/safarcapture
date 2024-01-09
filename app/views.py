from django.shortcuts import render
from django.views.generic import ListView, FormView
from app.forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
from app.models import Contact, Blog


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


def faq(request):
    return render(request, "faq.html")


def success(request):
    return render(request, "success.html")