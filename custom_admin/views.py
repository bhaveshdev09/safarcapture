from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from custom_admin.forms import CustomUserAuthForm
from django.contrib.auth.views import LogoutView
from app.models import Package


class CustomUserLoginView(FormView):
    form_class = CustomUserAuthForm
    template_name = "custom_admin/login.html"
    success_url = reverse_lazy("main")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(redirect_to=reverse_lazy("main"))
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


def booking_history(request):
    return render(request, "custom_admin/booking_history.html")


def customer_enquiry(request):
    return render(request, "custom_admin/customer_enquiry.html")


def destination(request):
    return render(request, "custom_admin/destination.html")


def main(request):
    return render(request, "custom_admin/main.html")


class PackageListView(ListView):
    model = Package
    template_name = "custom_admin/package_list.html"
    context_object_name = "packages"
    ordering = ["price"]
    paginate_by = 4

    def get_queryset(self):
        return Package.objects.all().order_by(*self.ordering)


def user_details(request):
    return render(request, "custom_admin/user_details.html")
