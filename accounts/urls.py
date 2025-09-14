from django.urls import path
from .views import SignupView, ProfileView, SettingsView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("settings/", SettingsView.as_view(), name="settings"),
]
