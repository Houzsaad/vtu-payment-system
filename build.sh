#manage.py migrate:
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

python manage.py shell -c"

from accounts.models import Costomer

if not Costomer.objects.filter(email='smahadi@admin.com').exists():
    Costomer.objects.create_superuser('smahadi@admin.com', '09065379803', 'smahadi0012026')
"