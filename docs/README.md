# Datis Website

A Django-based website for a small company to showcase its portfolio, projects, and services to clients. The user-facing interface is in Persian, while the admin panel supports both Farsi and English.

## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup and Install](#setup-and-install)
  - [Usage](#usage)
- [Show Your Support](#show-your-support)
- [License](#license)

## About the Project <a id="about-the-project"></a>

This repository contains a Django project for a mini company that needs an online presence. The website allows the company to present its portfolio, list services, and share project details with potential clients. The admin panel is bilingual (Persian/English) for easy management, while the public website is entirely in Persian.

### Built With <a id="built-with"></a>

#### Tech Stack <a id="tech-stack"></a>

- **Language**: Python
- **Framework**: Django
- **Database**: PostgreSQL
- **Containerization**: Docker

#### Key Features <a id="key-features"></a>

- Company portfolio and project showcase
- Service listing pages
- Bilingual admin panel (Farsi and English)
- User‑facing interface in Persian
- Django’s built‑in admin interface for content management

## Getting Started <a id="getting-started"></a>

Follow these steps to run the project locally.

### Prerequisites <a id="prerequisites"></a>

```sh
git
docker
docker-compose
```

### Setup and Install <a id="setup-and-install"></a>

Clone the repository and start the application using Docker Compose.

```sh
# Clone the repository
git clone https://github.com/geekmanesh/datis-website.git
cd datis-website

# Build and run the containers
docker-compose up --build
```

The first run will build the Django image, set up the PostgreSQL database, and apply migrations automatically.

### Usage

Once the containers are running, open your browser and go to:

- **Website**: [http://localhost:8000](http://localhost:8000) – the public Persian site.
- **Admin Panel**: [http://localhost:8000/admin](http://localhost:8000/admin) – log in with the superuser credentials you created.

The admin interface can be switched between Farsi and English via Django’s language selector.

## Show Your Support

If you find this project interesting, please give it a star on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.