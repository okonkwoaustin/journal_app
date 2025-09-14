from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "first_name",
            "last_name",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "first_name",
            "last_name",
        )

class UserSettingsForm(forms.ModelForm):
    """
    A simple, user-friendly form for updating profile details.
    Extend fields if your CustomUser model has more attributes
    (like avatar, bio, etc.).
    """
    first_name = forms.CharField(
        label="First Name",
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "First name"})
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Last name"})
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "you@example.com"})
    )

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email"]