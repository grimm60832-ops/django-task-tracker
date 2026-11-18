from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from catalog.forms import (
    DeveloperUpdateForm,
    RegistrationForm,
    TaskCommentForm,
    TaskSearchForm,
)
from catalog.models import(
    Developer,
    Position,
    Project,
    Task,
    TaskComment
)

User = get_user_model()


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
    context_object_name = "project_list"
    paginate_by = 10

    def get_queryset(self):
        queryset_p = super().get_queryset()
        search_query = self.request.GET.get("q", "").strip()

        if search_query:
            queryset_p = queryset_p.filter(name__icontains=search_query)

        return queryset_p


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "catalog/project_detail.html"


class DeveloperListView(LoginRequiredMixin, ListView):
    model = Developer
    template_name = "catalog/developer_list.html"


class DeveloperCreateView(LoginRequiredMixin, CreateView):
    model = Developer
    fields = ["username", "first_name", "last_name", "position"]
    template_name = "catalog/developer_form.html"
    success_url = reverse_lazy("catalog:developers")

    def form_valid(self, form):
        messages.success(self.request, "Successfully created a new developer.")
        return super().form_valid(form)


class DeveloperDetailView(LoginRequiredMixin, DetailView):
    model = Developer
    template_name = "catalog/developer_detail.html"


class DeveloperUpdateView(LoginRequiredMixin, UpdateView):
    model = Developer
    template_name = "catalog/dev_profile.html"
    form_class = DeveloperUpdateForm
    success_url = reverse_lazy("catalog:developers")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Successfully updated your developer.")
        return super().form_valid(form)


class DeveloperDeleteView(LoginRequiredMixin, DeleteView):
    model = Developer
    template_name = "catalog/developer_confirm_delete.html"
    success_url = reverse_lazy("catalog:developers")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Developer successfully deleted.")
        return super().delete(request, *args, **kwargs)


class PositionListView(LoginRequiredMixin, ListView):
    model = Position
    template_name = "catalog/position_list.html"


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "catalog/task_list.html"
    context_object_name = "task_list"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        status = self.request.GET.get("status")
        priority = self.request.GET.get("priority")

        if name:
            queryset = queryset.filter(name__icontains=name)
        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = TaskSearchForm(self.request.GET)
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = [
        "name",
        "description",
        "deadline",
        "is_completed",
        "priority",
        "project",
        "assignees",
    ]
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:tasks")

    def form_valid(self, form):
        messages.success(self.request, "Successfully created a new task.")
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "catalog/task_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskCommentForm()
        context["status_choices"] = Task.StatusChoices.choices
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        new_status = request.POST.get("new_status")
        if new_status in dict(Task.StatusChoices.choices):
            self.object.status = new_status
            if new_status == Task.StatusChoices.DONE:
                self.object.is_completed = True
            else:
                self.object.is_completed = False
            self.object.save()
            messages.success(request, "Task status successfully updated.")
            return redirect("catalog:task-detail", pk=self.object.pk)

        form = TaskCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = self.object
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect("catalog:task-detail", pk=self.object.pk)

        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = [
        "name",
        "description",
        "deadline",
        "is_completed",
        "priority",
        "project",
        "assignees",
    ]
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


class TaskCommentDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskComment

    def get_success_url(self):
        return reverse_lazy("catalog:task-detail", kwargs={"pk": self.object.task.pk})

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user and not request.user.is_staff:
            messages.error(request, "You can only delete your own comments.")
            return redirect("catalog:task-detail", pk=comment.task.pk)
        return super().dispatch(request, *args, **kwargs)


class RegistrationView(generic.CreateView):
    form_class = RegistrationForm
    template_name = "catalog/register.html"
    success_url = reverse_lazy("catalog:login")


class CustomLogoutView(LoginRequiredMixin, AuthLogoutView):
    next_page = reverse_lazy("catalog:index")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Successfully logged out")
        return super().dispatch(request, *args, **kwargs)
