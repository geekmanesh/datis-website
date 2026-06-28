from projects.models import Project

from .models import SiteConfig


def site_configuration(request):
    return {
        "site_config": SiteConfig.load(),
        "recent_projects": Project.objects.all()[:3],
    }
