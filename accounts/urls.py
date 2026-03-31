
from django.contrib import admin
from django.urls import path
from .import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',v.signup_view , name='signup'),
    path("login", v.login_view, name="login"),
    path("logout", v.logout_view, name="logout"),
    path("add-address/", v.add_address, name="add_address"),
    path("edit-address/<int:address_id>/", v.edit_address, name="edit_address"),
    path("delete-address/<int:address_id>/", v.delete_address, name="delete_address"),


     path(
        "reset-password/",
        auth_views.PasswordResetView.as_view(
            template_name="password_reset.html",
            email_template_name="password_reset_email.html",
            subject_template_name="password_reset_subject.txt",
            success_url="/accounts/reset-password/done/",
        ),
        name="password_reset",
    ),

    path(
        "reset-password/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_done.html",
        ),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html",
            success_url="/accounts/reset/done/",
        ),
        name="password_reset_confirm",
    ),

    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
]
