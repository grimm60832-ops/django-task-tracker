from django.urls import path
from django.contrib.auth.views import LoginView
from catalog.views import (
    IndexView,
    DeveloperListView,
    PositionListView,
    ProjectListView,
    TaskListView,
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
    path('developers/', DeveloperListView.as_view(), name="developers"),
    path('positions/', PositionListView.as_view(), name="positions"),
    path('tasks/', TaskListView.as_view(), name="tasks"),
    path('login/', LoginView.as_view(template_name="catalog/login.html"), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('register/', RegistrationView.as_view(), name="register"),
    path('profile/', DeveloperUpdateView.as_view(), name="dev_profile"),
    path('project/create/', ProjectCreateView.as_view(), name="project-create"),
    path('project/update/<int:pk>/', ProjectUpdateView.as_view(), name="project-update"),
    path('project/delete/<int:pk>/', ProjectDeleteView.as_view(), name="project-delete"),
    path('project/detail/<int:pk>/', ProjectDetailView.as_view(), name="project-detail"),
)
