SHELL := /bin/bash
.DEFAULT_GOAL := help

DC        := docker compose
WEB       := web
DB        := db
MANAGE    := $(DC) exec $(WEB) python manage.py
PSQL      := $(DC) exec $(DB) psql

##@ Help

.PHONY: help
help: ## Show this help message
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} \
		/^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } \
		/^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) }' $(MAKEFILE_LIST)

##@ Getting Started

.PHONY: env
env: ## Create .env from .env-example if it doesn't exist yet
	@test -f .env && echo ".env already exists, skipping." || (cp .env-example .env && echo "Created .env — update it with real secrets before deploying.")

.PHONY: bootstrap
bootstrap: env build up migrate ## First-time setup: create .env, build images, start stack, run migrations
	@echo "Bootstrap complete. Run 'make superuser' to create an admin account, then visit http://localhost:8000"

##@ Docker Lifecycle

.PHONY: build
build: ## Build (or rebuild) the docker images
	$(DC) build

.PHONY: rebuild
rebuild: ## Rebuild docker images from scratch, without cache
	$(DC) build --no-cache

.PHONY: up
up: ## Start the stack in the background
	$(DC) up -d

.PHONY: upf
upf: ## Start the stack in the foreground (logs attached)
	$(DC) up

.PHONY: down
down: ## Stop the stack, keeping data volumes
	$(DC) down

.PHONY: down-v
down-v: ## Stop the stack and remove data volumes (destroys the database!)
	$(DC) down --volumes

.PHONY: restart
restart: down up ## Restart the stack

.PHONY: ps
ps: ## Show status of running containers
	$(DC) ps

.PHONY: logs
logs: ## Tail logs for all services
	$(DC) logs -f

.PHONY: logs-web
logs-web: ## Tail logs for the web service only
	$(DC) logs -f $(WEB)

.PHONY: logs-db
logs-db: ## Tail logs for the db service only
	$(DC) logs -f $(DB)

.PHONY: shell
shell: ## Open a bash shell inside the web container
	$(DC) exec $(WEB) bash

##@ Django Management

.PHONY: migrate
migrate: ## Apply database migrations
	$(MANAGE) migrate

.PHONY: makemigrations
makemigrations: ## Create new migrations based on model changes
	$(MANAGE) makemigrations

.PHONY: superuser
superuser: ## Create a Django superuser (interactive)
	$(MANAGE) createsuperuser

.PHONY: django-shell
django-shell: ## Open the Django interactive shell
	$(MANAGE) shell

.PHONY: dbshell
dbshell: ## Open a psql shell on the running database
	$(MANAGE) dbshell

.PHONY: collectstatic
collectstatic: ## Collect static files
	$(MANAGE) collectstatic --no-input

.PHONY: check
check: ## Run Django's system checks
	$(MANAGE) check

.PHONY: makemessages
makemessages: ## Extract translatable strings into .po files
	$(MANAGE) makemessages -a

.PHONY: compilemessages
compilemessages: ## Compile .po files into .mo files
	$(MANAGE) compilemessages

##@ Testing & Quality (run locally via uv, matches CI)

.PHONY: install
install: ## Install/sync all dependencies, including dev tools
	uv sync --dev

.PHONY: test
test: ## Run the Django test suite
	uv run python manage.py test --verbosity=2

.PHONY: lint
lint: ## Check code style with ruff
	uv run ruff check .

.PHONY: lint-fix
lint-fix: ## Auto-fix lint issues with ruff
	uv run ruff check . --fix

.PHONY: format
format: ## Format code with ruff
	uv run ruff format .

.PHONY: format-check
format-check: ## Check code formatting without changing files
	uv run ruff format . --check

.PHONY: djlint
djlint: ## Check template formatting with djlint
	uv run djlint templates --check

.PHONY: djlint-fix
djlint-fix: ## Auto-reformat templates with djlint
	uv run djlint templates --reformat

.PHONY: quality
quality: lint format-check djlint ## Run all quality checks (mirrors CI "Code Quality" job)

##@ Cleanup

.PHONY: clean
clean: ## Remove Python bytecode and cache files
	find . -type d -name "__pycache__" -not -path "./.venv/*" -exec rm -rf {} +
	find . -type f -name "*.pyc" -not -path "./.venv/*" -delete
	rm -rf .ruff_cache .pytest_cache

.PHONY: prune
prune: ## Remove stopped containers, dangling images and unused networks
	docker system prune -f
