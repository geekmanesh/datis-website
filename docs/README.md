# Datis

Datis is the website for a small company, built to present its services, past
projects, and general information to clients. The public site is in Persian;
the admin panel supports both Persian and English.

## Features

- Homepage with hero section, services overview, and recent projects
- Services listing and detail pages
- Projects listing and detail pages, grouped by category, with image galleries
- About page
- Contact page with a message form (rate-limited per IP)
- Admin panel built on django-unfold, with a language switcher
- Site-wide settings (company name, contact info, social links, hero text)
  managed as a single record in the admin panel

## Tech stack

- Python 3.14
- Django 6
- PostgreSQL 17
- django-unfold for the admin interface
- django-solo for the single-record site settings
- uv for dependency management
- Docker / Docker Compose for local development and deployment
- ruff and djlint for linting and formatting

## Project layout

- `datis/` - project settings, URLs, WSGI/ASGI entrypoints
- `core/` - site settings, homepage, about and contact pages
- `services/` - service listing and detail pages
- `projects/` - project listing, detail pages, and categories
- `users/` - custom user model (email-based authentication)
- `templates/` - HTML templates, organized by page and shared components
- `static/`, `media/` - static assets and uploaded files
- `locale/` - translation files

## Getting started

### Requirements

- Docker and Docker Compose
- `make` (optional, but recommended - see below)

### Setup

Clone the repository and create your local environment file:

```sh
git clone git@github.com:geekmanesh/datis-website.git
cd datis-website
cp .env-example .env
```

Update `.env` with your own values (`SECRET_KEY`, database name, user, and
password).

Build the images and start the stack:

```sh
docker compose up --build
```

This starts two containers: `web` (the Django app, served on port 8000) and
`db` (PostgreSQL 17). Once the containers are up, apply migrations and create
an admin account:

```sh
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

### Using the Makefile

A `Makefile` is included to wrap the commands above. Run `make help` to list
everything available, grouped by category (Docker lifecycle, Django
management, testing and code quality, cleanup). A few examples:

```sh
make bootstrap    # create .env, build images, start the stack, run migrations
make up            # start the stack in the background
make migrate       # apply database migrations
make superuser     # create an admin account
make logs          # tail logs for all services
make down          # stop the stack
```

### Usage

- Website: http://localhost:8000
- Admin panel: http://localhost:8000/admin

## Running tests and checks locally

Install dependencies with `uv`:

```sh
uv sync --dev
```

Then run:

```sh
uv run python manage.py test
uv run ruff check .
uv run ruff format . --check
uv run djlint templates --check
```

These are the same checks run in CI on every push and pull request.

## Internationalization

The site supports Persian (default, public-facing) and English (admin panel).
Translation files live under `locale/`. After changing translatable strings,
regenerate and compile them with:

```sh
python manage.py makemessages -a
python manage.py compilemessages
```

## Contributing

See `docs/CODE_OF_CONDUCT.md` before opening an issue or pull request.

## License

MIT License. See [LICENSE](LICENSE) for details.
