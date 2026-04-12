#manage.py migrate:
#!/usr/bin/env bash
set -o errexit

pip -r install requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate