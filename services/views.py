from django.views.generic import TemplateView


class ServicesList(TemplateView):
    template_name = "pages/services.html"
