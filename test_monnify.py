import os
from urllib import response
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_webapp.settings')
django.setup()
print("Django setup done")

import requests
import base64
from django.conf import settings
print("API KEY:", settings.MONNIFY_API_KEY)
print("bASE URL:", settings.MONNIFY_BASE_URL)
print("SECRET KEY:", settings.MONNIFY_SECRET_KEY)
print("CONTRACT CODE:", settings.MONNIFY_CONTRACT_CODE)

#def get_monnify_token():
credentials = f"{settings.MONNIFY_API_KEY}: {settings.MONNIFY_SECRET_KEY}"
encoded = base64.b64encode(credentials.encode()).decode()

response = requests.post(
    f"{settings.MONNIFY_BASE_URL}/api/v1/auth/login",
    headers={"Authorization": f"Basic {encoded}"}
)
print(response.status_code)
print(response.json())