from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from catalog.models import Developer, TaskComment, Task

User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email",)


class DeveloperUpdateForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ("username", "first_name", "last_name", "position", "email",)


class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = TaskComment
        fields = ("comment",)


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Search by task name...",
            }
        ),
    )
    status = forms.ChoiceField(
        choices=[("", "All Statuses")] + list(Task.StatusChoices.choices),
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    priority = forms.ChoiceField(
        choices=[("", "All Priorities")] + list(Task.PriorityChoices.choices),
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
