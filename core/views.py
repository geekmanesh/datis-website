from django.views.generic import TemplateView

from services.models import Service


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()[:10]
        return context


class AboutPageView(TemplateView):
    template_name = "about-us/about-us.html"


class ContactPageView(TemplateView):
    template_name = "contact-us/contact-us.html"
