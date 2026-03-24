FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=config.settings

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# collectstatic needs env Django can read during build
ENV DJANGO_SECRET_KEY=build-only-not-for-production \
    DJANGO_DEBUG=False \
    DJANGO_ALLOWED_HOSTS=localhost

RUN python manage.py collectstatic --noinput

RUN chmod +x deploy/docker-entrypoint.sh

EXPOSE 8000

CMD ["deploy/docker-entrypoint.sh"]
