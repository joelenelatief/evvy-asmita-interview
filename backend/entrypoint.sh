#!/bin/sh

# qucik exit on error
set -o errexit

# migrations
python manage.py migrate

# static files
python manage.py collectstatic --noinput

# startup scripts
python manage.py staging_hydrate

# start server
gunicorn --config gunicorn.conf --bind 0.0.0.0:${PORT:-8000} wsgi:application --workers 2
