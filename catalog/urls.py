from django.urls import path
from catalog.views import IndexView
from catalog.views import ProjectListView


app_name = "catalog"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('projects/', ProjectListView.as_view(), name="projects"),
]
