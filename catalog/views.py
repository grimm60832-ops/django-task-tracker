from django.views.generic import (
    TemplateView,
    ListView,
    UpdateView,
    CreateView,
    DeleteView, DetailView,
)
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from catalog.forms import RegistrationForm, DeveloperUpdateForm


from catalog.models import Developer, Project, Task, Position


class IndexView(TemplateView):
    template_name = "catalog/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context["num_developers"] = Developer.objects.count()
        context["num_projects"] = Project.objects.count()
        context["num_tasks"] = Task.objects.count()
        context["num_positions"] = Position.objects.count()
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ["name", "description"]
    template_name = "catalog/project_form.html"
    success_url = reverse_lazy("catalog:projects")

    def form_valid(self, form):
        messages.success(self.request, "Successfully created a new project.")
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ["name", "description"]
    template_name = "catalog/project_form.html"
    success_url = reverse_lazy("catalog:projects")

    def form_valid(self, form):
        messages.success(self.request, "Successfully updated your project.")
        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "catalog/project_confirm_delete.html"
    success_url = reverse_lazy("catalog:projects")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Project successfully deleted.")
        return super().delete(request, *args, **kwargs)

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "catalog/project_list.html"


class ProjectDetailView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "catalog/project_delete.html"


class DeveloperListView(LoginRequiredMixin, ListView):
    model = Developer
    template_name = "catalog/developer_list.html"


class PositionListView(LoginRequiredMixin, ListView):
    model = Position
    template_name = "catalog/position_list.html"


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "catalog/task_list.html"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["name", "description", "deadline", "is_completed", "priority"]
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:tasks")

    def form_valid(self, form):
        messages.success(self.request, "Successfully created a new task.")
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "catalog/task_detail.html"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["name", "description", "deadline", "is_completed", "priority"]
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:tasks")

    def form_valid(self, form):
        messages.success(self.request, "Successfully updated your task.")
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "catalog/task_confirm_delete.html"
    success_url = reverse_lazy("catalog:tasks")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Successfully deleted your task.")
        return super().delete(request, *args, **kwargs)
    

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


class CustomLogoutView(LoginRequiredMixin, AuthLogoutView):
    next_page = reverse_lazy("catalog:index")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Successfully logged out")
        return super().dispatch(request, *args, **kwargs)
