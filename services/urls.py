from django.urls import path

from .views import ServicesList, ServiceDetial

urlpatterns = [
    path("", ServicesList.as_view(), name="services"),
    path("<slug:slug>/", ServiceDetial.as_view(), name="service-detail"),
]
