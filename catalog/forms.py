from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from catalog.models import Developer

User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email",)


class DeveloperUpdateForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ("username", "first_name", "last_name", "position", "email",)
