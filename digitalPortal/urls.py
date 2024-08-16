from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path("", include("digitalPortal.common.urls")),
    path("accounts/", include("digitalPortal.accounts.urls")),
    path("automations/", include("digitalPortal.automations.urls")),
    path("trackers/", include("digitalPortal.trackers.urls")),
    path("about/", include("digitalPortal.about.urls"))
)
