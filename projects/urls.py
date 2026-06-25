from django.urls import path

from .views import ProjectDetailView, ProjectsListView

urlpatterns = [
    path("", ProjectsListView.as_view(), name="projects"),
    path("<slug:slug>/", ProjectDetailView.as_view(), name="project-detail"),
]
