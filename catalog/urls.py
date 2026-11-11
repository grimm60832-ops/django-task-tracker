from django.urls import path
from catalog.views import (
    IndexView,
    DeveloperListView,
    PositionListView,
    ProjectListView,
    TaskListView
)


app_name = "catalog"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('projects/', ProjectListView.as_view(), name="projects"),
    path('developers/', DeveloperListView.as_view(), name="developers"),
    path('positions/', PositionListView.as_view(), name="positions"),
    path('tasks/', TaskListView.as_view(), name="tasks"),
]
