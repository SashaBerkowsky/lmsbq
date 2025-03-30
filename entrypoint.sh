#!/bin/bash

python manage.py migrate --noinput

echo "Creating superuser with username: $DJANGO_SUPERUSER_USERNAME and email: $DJANGO_SUPERUSER_EMAIL"
python manage.py shell <<EOF

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
    print('Superuser created.')
else:
    print('Superuser already exists.')
EOF
exec python manage.py runserver 0.0.0.0:8000
