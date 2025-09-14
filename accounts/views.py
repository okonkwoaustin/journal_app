from django.views.generic import CreateView, TemplateView, UpdateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserSettingsForm
from . models import CustomUser

class SignupView(CreateView):    
    """Register a new user."""

    form_class = UserRegistrationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")

class ProfileView(LoginRequiredMixin, TemplateView):
    """Display the logged-in user's profile."""
    template_name = "users/profile.html"

class SettingsView(LoginRequiredMixin, UpdateView):
    """
    Allow the logged-in user to update their own settings/profile.
    """
    model = CustomUser
    form_class = UserSettingsForm
    template_name = "users/settings.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user
