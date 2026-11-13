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
    CustomLogoutView
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
    path("profile/", DeveloperUpdateView.as_view(), name="dev_profile"),
)
