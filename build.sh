#manage.py migrate:
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
#python manage.py loaddata services/fixtures/initial_data.json
python manage.py shell -c"
import os
from accounts.models import Costomer
email = os.environ.get('ADMIN_EMAIL')
phone_number = os.environ.get('ADMIN_PHONE')
password = os.environ.get('ADMIN_PASSWORD')

if not Costomer.objects.filter(email=email).exists():
    Costomer.objects.create_superuser(email, phone_number, password)
"