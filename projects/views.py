from django.views.generic import TemplateView


class ProjectsList(TemplateView):
    template_name = "pages/projects.html"
