from django.urls import path

from .views import ServicesList

urlpatterns = [
    path("", ServicesList.as_view(), name="services"),
]
