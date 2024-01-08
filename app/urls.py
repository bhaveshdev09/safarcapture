from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blogs/", views.about, name="blogs"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("faq/", views.faq, name="faq"),
    path("success/", views.success, name="success"),
]
