from django.views.generic import TemplateView, ListView, UpdateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from catalog.forms import RegistrationForm, DeveloperUpdateForm


from catalog.models import Developer, Project, Task, Position


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "catalog/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context["num_developers"] = Developer.objects.count()
        context["num_projects"] = Project.objects.count()
        context["num_tasks"] = Task.objects.count()
        context["num_positions"] = Position.objects.count()
        return context


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "catalog/project_list.html"


class DeveloperListView(LoginRequiredMixin, ListView):
    model = Developer
    template_name = "catalog/developer_list.html"


class PositionListView(LoginRequiredMixin, ListView):
    model = Position
    template_name = "catalog/position_list.html"


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "catalog/task_list.html"


class RegistrationView(generic.CreateView):
    form_class = RegistrationForm
    template_name = "catalog/register.html"
    success_url = reverse_lazy("catalog:login")


class DeveloperUpdateView(LoginRequiredMixin, UpdateView):
    form_class = DeveloperUpdateForm
    template_name = "catalog/dev_profile.html"
    success_url = reverse_lazy("catalog:developers")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Successfully updated your developer profile.")
        return super().form_valid(form)
