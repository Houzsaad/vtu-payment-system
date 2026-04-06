from email.mime import message

import requests
from django.conf import settings

def get_headers():
    return {
        'api-key': settings.VTPASS_API_KEY,
        'public-key': settings.VTPASS_PUBLIC_KEY,
        'secret-key': settings.VTPASS_SECRET_KEY,
        'Content-type': 'application/json'
    }

def  purchase_data(phone_number, service_id, variation_code, amount, reference):
    url =  f"{settings.VTPASS_BASE_URL}/pay"
    payload = {
        'request_id': str(reference),
        'serviceID': service_id,
        'billersCode': phone_number,
        'variation_code': variation_code,
        'amount': str(amount),
        'phone': phone_number
    }
    print('URL:', url)
    print('Payload:', payload)
    print('Headers:', get_headers())
    response = requests.post(url, json=payload, headers=get_headers())
    print('Raw response:', response.text)
    print('Status code:', response.status_code)
    try:
        return response.json()
    except Exception:
        return {'code': 'error', 'message': response.text}
    

def purchase_airtime(phone_number, service_id, amount, reference):
    url = F"{settings.VTPASS_BASE_URL}/pay"
    payload = {
        'request_id': str(reference),
        'serviceID': service_id,
        'amount': str(amount),
        'phone': phone_number
    }
    response = requests.post(url, json=payload, headers=get_headers())
    print('Raw response:', response.text)
    print('Status code:', response.status_code)
    try:
        return response.json()
    except Exception:
        return {'code': 'error', 'message': response.text}
    


    