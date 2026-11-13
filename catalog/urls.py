from django.urls import path
from django.contrib.auth.views import LoginView
from catalog.views import (
    IndexView,
    DeveloperListView,
    DeveloperCreateView,
    DeveloperUpdateView,
    DeveloperDeleteView,
    DeveloperDetailView,
    PositionListView,
    ProjectListView,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    RegistrationView,
    DeveloperUpdateView,
    CustomLogoutView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    ProjectDetailView,


)


app_name = "catalog"

urlpatterns = (
    path('', IndexView.as_view(), name="index"),
    path('projects/', ProjectListView.as_view(), name="projects"),
    path('project/create/', ProjectCreateView.as_view(), name="project-create"),
    path('project/update/<int:pk>/', ProjectUpdateView.as_view(), name="project-update"),
    path('project/delete/<int:pk>/', ProjectDeleteView.as_view(), name="project-delete"),
    path('project/detail/<int:pk>/', ProjectDetailView.as_view(), name="project-detail"),
    path('developers/', DeveloperListView.as_view(), name="developers"),
    path('developer/create/', DeveloperCreateView.as_view(), name="developer-create"),
    path('developers/<int:pk>/', DeveloperDetailView.as_view(), name='developer-detail'),
    path('developers/<int:pk>/update/', DeveloperUpdateView.as_view(), name='developer-update'),
    path('developers/<int:pk>/delete/', DeveloperDeleteView.as_view(), name='developer-delete'),
    path('positions/', PositionListView.as_view(), name="positions"),
    path('tasks/', TaskListView.as_view(), name="tasks"),
    path('task/create/', TaskCreateView.as_view(), name="task-create"),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name="task-update"),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name="task-delete"),
    path('task/detail/<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
    path('login/', LoginView.as_view(template_name="catalog/login.html"), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('register/', RegistrationView.as_view(), name="register"),
    path('profile/', DeveloperUpdateView.as_view(), name="dev_profile"),

)
