from django.urls import path

from .views import ServiceDetailView, ServicesListView

urlpatterns = [
    path("", ServicesListView.as_view(), name="services"),
    path("<slug:slug>/", ServiceDetailView.as_view(), name="service-detail"),
]
