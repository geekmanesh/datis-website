from django.views.generic import DetailView, ListView

from .models import Service


class ServicesListView(ListView):
    model = Service
    template_name = "services/list.html"
    context_object_name = "services"


class ServiceDetailView(DetailView):
    model = Service
    template_name = "services/detail.html"
    context_object_name = "service"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()[:10]
        return context
