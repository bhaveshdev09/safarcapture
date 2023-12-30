from django.urls import path
from myapp import views
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blogs/", views.about, name="blogs"),
    path("contact/", views.contact, name="contact"),
    path("faq/", views.faq, name="faq"),
    path("destination/", views.destination, name="destination"),
    path("thankyou/", views.thankyou, name="thankyou"),
    path("query_form/", views.query_form, name="query_form"),

    path("destination_admin/", views.destination_admin, name="destination_admin"),
    
]

