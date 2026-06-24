from django.urls import path

from .views import ServicesListView, ServiceDetailView

urlpatterns = [
    path("", ServicesListView.as_view(), name="services"),
    path("<slug:slug>/", ServiceDetailView.as_view(), name="service-detail"),
]
