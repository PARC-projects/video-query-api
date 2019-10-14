#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py loaddata 1-lookups

# Development
# python3 manage.py loaddata 2-dev-video 3-dev-search-set 4-dev-query 5-dev-results 6-dev-features 7-dev-video-clip

exec "$@"
