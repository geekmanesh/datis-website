from django.urls import path

from .views import ProjectsList, ProjectDetail

urlpatterns = [
    path("", ProjectsList.as_view(), name="projects"),
    path("<slug:slug>/", ProjectDetail.as_view(), name="project-detail"),
]
