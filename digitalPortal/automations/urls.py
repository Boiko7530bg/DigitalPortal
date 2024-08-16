from django.urls import path, include

from digitalPortal.automations.views import details_automation, add_automation, edit_automation, delete_automation, \
    automation_home

urlpatterns = (
    path("", automation_home, name="automation home"),
    path("add/", add_automation, name="add automation"),
    path("<int:pk>/", include(
        [
            path("", details_automation, name="details automation"),
            path("edit/", edit_automation, name="edit automation"),
            path("delete/", delete_automation, name="delete automation"),
        ]
    )),
)
