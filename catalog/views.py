from django.views.generic import TemplateView
from django.views.generic import ListView
from django.shortcuts import render

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


class ProjectListView(ListView):
    model = Project
    template_name = "catalog/project_list.html"


class DeveloperListView(ListView):
    model = Developer
    template_name = "catalog/developer_list.html"