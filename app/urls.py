from django.urls import path
from app import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("blogs/", views.BlogListView.as_view(), name="blogs"),
    path("blogs/details/<pk>/", views.BlogDetailView.as_view(), name="blog-detail"),
    path(
        "packages/details/<pk>/",
        views.PackageDetailView.as_view(),
        name="package-detail",
    ),
    path(
        "packages/booking/",
        views.post_booking,
        name="package-booking",
    ),
    path(
        "destinations/details/<pk>/",
        views.DestinationDetailView.as_view(),
        name="destination-detail",
    ),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("faq/", views.FAQView.as_view(), name="faq"),
    path("gallary/", views.GalleryView.as_view(), name="gallery"),
    path("success/", views.SuccessView.as_view(), name="success"),
    path(
        "terms-condtions/", views.TermsConditionView.as_view(), name="terms-conditions"
    ),
    path("privacy-policy/", views.PrivacyPolicyView.as_view(), name="privacy-policy"),
]
