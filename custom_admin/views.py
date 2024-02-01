from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView, TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from custom_admin.forms import (
    CustomUserAuthForm,
    PackageForm,
    InclusiveFormSet,
    ExclusiveFormSet,
    IternaryFormSet,
    BookingForm,
)
from app.models import Package, Booking
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomUserLoginView(FormView):
    form_class = CustomUserAuthForm
    template_name = "custom_admin/login.html"
    success_url = reverse_lazy("admin-dashboard")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(redirect_to=reverse_lazy("admin-dashboard"))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        print(form.cleaned_data)
        user = authenticate(self.request, email=email, password=password)
        print(user)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid credentials")
            return self.form_invalid(form)

    def form_invalid(self, form):
        print(form.errors)
        response = super().form_invalid(form)
        for message in form.errors.values():
            messages.error(
                self.request,
                message[0],
            )

        return response


class CustomUserLogoutView(LogoutView):
    next_page = reverse_lazy("admin-login")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been successfully logged out.")
        return super().dispatch(request, *args, **kwargs)


def customer_enquiry(request):
    return render(request, "custom_admin/customer_enquiry.html")


def destination(request):
    return render(request, "custom_admin/destination.html")


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "custom_admin/main.html"
    login_url = reverse_lazy("admin-login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        bookings_confirm_count = Booking.objects.filter(
            status=Booking.STATUS_COMPLETED
        ).count()
        packages = Package.objects.all().count()
        bookings = Booking.objects.all().order_by("-created_at")[:5]

        context["total_booking"] = bookings_confirm_count
        context["total_queries"] = packages
        context["bookings"] = bookings

        return context


class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking_update.html"
    success_url = reverse_lazy("booking_list")


class BookingDeleteView(DeleteView):
    model = Booking
    template_name = "booking_delete.html"
    success_url = reverse_lazy("booking_list")


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "custom_admin/booking_list.html"
    context_object_name = "bookings"
    paginate_by = 2
    login_url = reverse_lazy("admin-login")

    queryset = Booking.objects.all().order_by("-created_at")


class PackageListView(LoginRequiredMixin, ListView):
    model = Package
    template_name = "custom_admin/package_list.html"
    context_object_name = "packages"
    ordering = ["price"]
    paginate_by = 4
    login_url = reverse_lazy("admin-login")

    def get_queryset(self):
        return Package.objects.all().order_by(*self.ordering)


class PackageCreateView(CreateView):
    model = Package
    form_class = PackageForm
    template_name = "custom_admin/package_form.html"
    success_url = reverse_lazy("package-list")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["inclusives"] = InclusiveFormSet(
                instance=self.object, prefix="inclusive"
            )
            data["exclusives"] = ExclusiveFormSet(
                instance=self.object, prefix="exclusive"
            )
            data["iternaries"] = IternaryFormSet(
                instance=self.object, prefix="iternary"
            )
            # data['books'] = BookFormSet(self.request.POST, instance=self.object)
            # data['genres'] = GenreFormSet(self.request.POST)
        else:
            data["inclusives"] = InclusiveFormSet(instance=self.object)
            data["exclusives"] = ExclusiveFormSet(instance=self.object)
            data["iternaries"] = IternaryFormSet(instance=self.object)
            # data['genres'] = GenreFormSet()
        return data

    def form_invalid(self, form):
        print(form.errors)
        response = super().form_invalid(form)
        return response


class PackageUpdateView(UpdateView):
    model = Package
    form_class = PackageForm
    template_name = "custom_admin/package_form.html"
    success_url = reverse_lazy("package-list")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["inclusives"] = InclusiveFormSet(
                instance=self.object, prefix="inclusive"
            )
            data["exclusives"] = ExclusiveFormSet(
                instance=self.object, prefix="exclusive"
            )
            data["iternaries"] = IternaryFormSet(
                instance=self.object, prefix="iternary"
            )
            # data['books'] = BookFormSet(self.request.POST, instance=self.object)
            # data['genres'] = GenreFormSet(self.request.POST)
        else:
            data["inclusives"] = InclusiveFormSet(instance=self.object)
            data["exclusives"] = ExclusiveFormSet(instance=self.object)
            data["iternaries"] = IternaryFormSet(instance=self.object)
            # data['genres'] = GenreFormSet()
        return data


def user_details(request):
    return render(request, "custom_admin/user_details.html")
