from django.urls import path

from .views import ProjectDetail, ProjectsList

urlpatterns = [
    path("", ProjectsList.as_view(), name="projects"),
    path("<slug:slug>/", ProjectDetail.as_view(), name="project-detail"),
]
