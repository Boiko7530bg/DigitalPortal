from django.urls import path, include

from digitalPortal.trackers.views import add_tracker, delete_tracker, details_tracker, edit_tracker

urlpatterns = (
    path("add/", add_tracker, name="add tracker"),
    path("<int:pk>/", include(
        [
            path("", details_tracker, name="details tracker"),
            path("edit/", edit_tracker, name="edit tracker"),
            path("delete/", delete_tracker, name="delete tracker"),
        ],
    ))
)