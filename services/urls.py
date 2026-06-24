from django.urls import path

from .views import ServicesListView

urlpatterns = [
    path("", ServicesListView.as_view(), name="services"),
    path("<slug:slug>/", ServicesListView.as_view(), name="service-detail"),
]
