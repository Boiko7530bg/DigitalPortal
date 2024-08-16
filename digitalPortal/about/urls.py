from django.urls import path

from digitalPortal.about.views import about

urlpatterns = (
    path("", about, name="about"),
)