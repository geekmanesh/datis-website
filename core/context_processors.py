from .models import SiteConfig


def site_configuration(request):
    return {"site_config": SiteConfig.load()}
