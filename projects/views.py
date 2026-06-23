from django.views.generic import TemplateView


class ProjectsList(TemplateView):
    template_name = "pages/projects.html"


class ProjectDetail(TemplateView):
    template_name = "pages/projects-details.html"
