from django.urls import path
from custom_admin import views

urlpatterns = [
    path("login/", views.CustomUserLoginView.as_view(), name="admin-login"),
    path("logout/", views.CustomUserLogoutView.as_view(), name="admin-logout"),
    path(
        "customer-enquiry/",
        views.CustomerEnquiryListView.as_view(),
        name="admin-customer-enquiry",
    ),
    path("destination/", views.destination, name="destination"),
    path("dashboard/", views.DashboardView.as_view(), name="admin-dashboard"),
    path("packages/", views.PackageListView.as_view(), name="admin-package-list"),
    path(
        "packages/create/",
        views.PackageCreateView.as_view(),
        name="admin-package-create",
    ),
    path(
        "packages/<int:pk>/update/",
        views.PackageUpdateView.as_view(),
        name="admin-package-update",
    ),
    path("user_details/", views.user_details, name="user_details"),
    path(
        "bookings/<int:pk>/update/",
        views.BookingUpdateView.as_view(),
        name="admin-booking-update",
    ),
    path(
        "bookings/<int:pk>/delete/",
        views.BookingDeleteView.as_view(),
        name="admin-booking-delete",
    ),
    path("bookings/list/", views.BookingListView.as_view(), name="admin-booking-list"),
    path("gallery/", views.AdminGalleryList.as_view(), name="admin-gallery"),
    # path(
    #     "booking-history/", views.booking_history, name="booking-history"
    # ),
]
