from django.contrib import messages
from django.core.cache import cache
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from projects.models import Project
from services.models import Service

from .forms import ContactMessageForm

CONTACT_FORM_COOLDOWN_SECONDS = 60


def _get_client_ip(request):
    forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded_for:
        return forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


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


class ContactPageView(FormView):
    template_name = "contact-us/contact-us.html"
    form_class = ContactMessageForm
    success_url = reverse_lazy("contact-us")

    def form_valid(self, form):
        ip_address = _get_client_ip(self.request)
        cache_key = f"contact-form-submit:{ip_address}"

        if ip_address and cache.get(cache_key):
            form.add_error(
                None,
                "شما اخیراً پیامی ارسال کرده‌اید. لطفاً کمی بعد دوباره تلاش کنید.",
            )
            return self.form_invalid(form)

        contact_message = form.save(commit=False)
        contact_message.ip_address = ip_address
        contact_message.save()

        if ip_address:
            cache.set(cache_key, True, CONTACT_FORM_COOLDOWN_SECONDS)

        messages.success(self.request, "پیام شما با موفقیت ارسال شد.")
        return super().form_valid(form)
