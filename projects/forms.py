from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        labels = {
            "name": "Project Title",
            "description": "Full Description",
            "customer": "Client Name",
            "cost": "Budget",
            "category": "Project Category",
            "status": "Project Status",
        }
