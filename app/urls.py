from django.urls import path
from app import views
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blogs/", views.about, name="blogs"),
    path("contact/", views.about, name="contact"),
    path("faq/", views.faq, name="faq"),
]