import requests
import base64
from django.conf import settings

def get_monnify_token():
    credentials = f"{settings.MONNIFY_API_KEY}: {settings.MONNIFY_SECRET_KEY}"
    encoded = base64.b64encode(credentials.encode()).decode()

    response = requests.post(
        f"{settings.MONNIFY_BASE_URL}/api/v1/auth/login",
        headers={"Authorization": f"Basic {encoded}"}
    )
    data = response.json()
    
    return data ['responseBody'] ['accessToken']

def create_virtual_account(costomer):
    token = get_monnify_token()

    payload = {

        "accountReference": str(costomer.id),
        "accountName": f"{costomer.email} {costomer.phone_number}",
        "currencyCode": "NGN",
        "contractCode": settings.MONNIFY_BUSINESS_CODE,
        "costomerEmail": costomer.email,
        "getAllAvailableBanks": False,
        "preferredBanks": ["035"] #Wema Bank [ALAT]
    }

    response = requests.post(
        f"{settings.MONNIFY_BASE_URL}/api/v2/bank-transfer/reserved-accounts",
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )
    
    return response.json()