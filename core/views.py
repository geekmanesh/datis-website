from django.views.generic import TemplateView

from projects.models import Project
from services.models import Service


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()[:10]
        context["projects"] = Project.objects.prefetch_related("images")[:5]
        return context


class AboutPageView(TemplateView):
    template_name = "about-us/about-us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()[0:3]
        return context


class ContactPageView(TemplateView):
    template_name = "contact-us/contact-us.html"
