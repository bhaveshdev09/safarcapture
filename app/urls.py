from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blogs/", views.BlogListView.as_view(), name="blogs"),
    path("blogs/details/<pk>/", views.BlogDetailView.as_view(), name="blog-detail"),
    path(
        "packages/details/<pk>/",
        views.PackageDetailView.as_view(),
        name="package-detail",
    ),
    path(
        "destinations/details/<pk>/",
        views.DestinationDetailView.as_view(),
        name="destination-detail",
    ),
    path(
        "packages/booking/",
        views.post_booking,
        name="package-booking",
    ),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("faq/", views.faq, name="faq"),
    path("gallary/", views.GalleryView.as_view(), name="gallery"),
    path("success/", views.success, name="success"),
    path("terms-condtions/", views.terms_conditions, name="terms-conditions"),
    path("privacy-policy/", views.privacy_policy, name="privacy-policy"),
]
