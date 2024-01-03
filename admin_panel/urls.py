from django.urls import path
from admin_panel import views
urlpatterns = [
    path("", views.dashboardlogin, name="dashboardlogin"),
    path("dashboardmain/", views.dashboardmain, name="dashboardmain"),
    path("logout/", views.handlelogout, name="handlelogout"),
]
