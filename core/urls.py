from django.urls import path

from .views import (
    AboutPageView,
    ContactPageView,
    HomePageView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about-us/", AboutPageView.as_view(), name="about-us"),
    path("contact-us/", ContactPageView.as_view(), name="contact-us"),
]
