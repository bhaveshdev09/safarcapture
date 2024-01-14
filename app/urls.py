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
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("faq/", views.faq, name="faq"),
    path("success/", views.success, name="success"),
]
