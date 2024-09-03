#!/bin/sh

echo "--- Applying Django Migrations ---"
python manage.py migrate
echo "--- Applying Django Collect Static ---"
python manage.py collectstatic --no-input --clear

exec "$@"