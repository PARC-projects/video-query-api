#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# https://docs.djangoproject.com/en/2.2/ref/django-admin/#flush
# Removes all data from the database and re-executes any post-synchronization handlers.
# The table of which migrations have been applied is not cleared.
# python manage.py flush --no-input

# Migrations
python manage.py migrate
python manage.py loaddata 1-lookups

# Development Migrations
# python3 manage.py loaddata 2-dev-video 3-dev-search-set 4-dev-query 5-dev-results 6-dev-features 7-dev-video-clip

# Use this if a STATIC_ROOT directory is specified for production in settings.py
python manage.py collectstatic --no-input --clear

exec "$@"
