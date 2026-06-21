from django.urls import path

from .views import ProjectsList

urlpatterns = [
    path("", ProjectsList.as_view(), name="projects"),
]
