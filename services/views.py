from django.views.generic import TemplateView


class ServicesList(TemplateView):
    template_name = "pages/services.html"


class ServiceDetial(TemplateView):
    template_name = "pages/services-details.html"
