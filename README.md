# WICI Uganda MVP Website

Django MVP website for Women in Construction & Infrastructure Ugandan Chapter (WICI Uganda).

## Tech stack
- Django
- HTML/CSS/JavaScript
- Bootstrap 5

## Setup
1. Create virtual environment:
   - `python3 -m venv .venv`
2. Install dependencies:
   - `./.venv/bin/pip install -r requirements.txt`
3. Run migrations:
   - `./.venv/bin/python manage.py migrate`
4. Start development server:
   - `./.venv/bin/python manage.py runserver`

## Project structure
- `config/` Django project configuration
- `website/` app with routes/views
- `templates/website/` page templates
- `static/website/` CSS, JS, images

## Implemented MVP pages
- `/` Home
- `/about/`
- `/programs/`
- `/events/`
- `/membership/`
- `/partners/`
- `/contact/`

## Deployment readiness checklist
Before production deployment, configure:
- `DEBUG = False`
- `ALLOWED_HOSTS` with production domain(s)
- HTTPS settings (`SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`)
- HSTS (`SECURE_HSTS_SECONDS` and related options)
- Strong production `SECRET_KEY` via environment variable
