from django.shortcuts import render


def admin_login(request):
    return render(request, "custom_admin/login.html")


def booking_history(request):
    return render(request, "custom_admin/booking_history.html")


def customer_enquiry(request):
    return render(request, "custom_admin/customer_enquiry.html")


def destination(request):
    return render(request, "custom_admin/destination.html")


def main(request):
    return render(request, "custom_admin/main.html")


def package(request):
    return render(request, "custom_admin/package.html")


def user_details(request):
    return render(request, "custom_admin/user_details.html")
