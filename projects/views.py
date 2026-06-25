from django.views.generic import DetailView, ListView

from .models import Category, Project


class ProjectsListView(ListView):
    model = Project
    template_name = "pages/projects.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.select_related("category").prefetch_related("images")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all()

        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "pages/projects-details.html"
    context_object_name = "project"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Project.objects.select_related("category").prefetch_related("images")
