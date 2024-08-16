from django.urls import path

from digitalPortal.common.views import index

urlpatterns = (
    path("", index, name="index"),
)
