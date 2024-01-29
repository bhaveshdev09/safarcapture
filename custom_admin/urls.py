from django.urls import path
from custom_admin import views

urlpatterns = [
    path("login/", views.CustomUserLoginView.as_view(), name="admin-login"),
    path("logout/", views.CustomUserLogoutView.as_view(), name="admin-logout"),
    path("booking-history/", views.booking_history, name="booking-history"),
    path("customer-enquiry/", views.customer_enquiry, name="customer-enquiry"),
    path("destination/", views.destination, name="destination"),
    path("dashboard/", views.main, name="main"),
    path("packages/", views.PackageListView.as_view(), name="admin-package-list"),
    path("user_details/", views.user_details, name="user_details"),
    # path(
    #     "booking-history/", views.booking_history, name="booking-history"
    # ),
]
