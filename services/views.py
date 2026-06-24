from django.views.generic import DetailView, ListView

from .models import Service


class ServicesListView(ListView):
    model = Service
    template_name = "pages/services.html"
    context_object_name = "services"


class ServiceDetailView(DetailView):
    model = Service
    template_name = "pages/services-details.html"
    context_object_name = "service"
    slug_field = "slug"
    slug_url_kwarg = "slug"
