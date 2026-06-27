from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home/index.html"


class AboutPageView(TemplateView):
    template_name = "about-us/about-us.html"


class ContactPageView(TemplateView):
    template_name = "contact-us/contact-us.html"
