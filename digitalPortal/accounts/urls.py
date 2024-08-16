from django.urls import path, include

from digitalPortal.accounts.views import signup_user, signin_user, signout_user, edit_user, delete_user, details_user

urlpatterns = (
    path("signup/", signup_user, name="signup user"),
    path("signin/", signin_user, name="signin user"),
    path("signout/", signout_user, name="signout user"),
    path("profile/<int:pk>/", include(
        [
            path("", details_user, name="details user"),
            path("edit/", edit_user, name="edit user"),
            path("delete/", delete_user, name="delete user"),
        ])
    )
)