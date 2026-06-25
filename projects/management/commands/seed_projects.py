import random
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand
from faker import Faker

from projects.models import Category, Project, ProjectImage

fake = Faker()


class Command(BaseCommand):
    help = "Create sample projects"

    def handle(self, *args, **kwargs):
        categories = []

        category_names = [
            "Construction",
            "Renovation",
            "Interior Design",
            "Painting",
            "Architecture",
            "Commercial",
        ]

        for name in category_names:
            category, _ = Category.objects.get_or_create(name=name)
            categories.append(category)

        seed_images = list(Path("media/seed").iterdir())

        for _ in range(40):
            project = Project.objects.create(
                name=fake.sentence(nb_words=3),
                description=fake.paragraph(nb_sentences=10),
                client=fake.company(),
                cost=fake.random_int(
                    min=1_000_000,
                    max=500_000_000,
                ),
                category=random.choice(categories),
                status=random.choice(
                    [
                        Project.StatusChoices.DONE,
                        Project.StatusChoices.IN_PROGRESS,
                    ]
                ),
            )

            image_count = random.randint(1, 5)

            for _ in range(image_count):
                image_path = random.choice(seed_images)

                with open(image_path, "rb") as image_file:
                    ProjectImage.objects.create(
                        project=project,
                        image=File(
                            image_file,
                            name=image_path.name,
                        ),
                    )

        self.stdout.write(self.style.SUCCESS("Created 6 categories and 40 projects."))
