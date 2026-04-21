import requests
import base64

from data_webapp import settings

API_KEY = "MK_TEST_VQ1909N3JW"
SECRET_KEY= "KBHFR7B0YZLYUGBCCBJ7L8WY289ZJHTF"

credentials = f"{API_KEY}: {SECRET_KEY}"
encoded = base64.b64encode(credentials.encode()).decode()
print("Encoded:", encoded)


response = requests.post(
    "https://sandbox.monnify.com/api/v1/auth/login",
    headers={"Authorization": f"Basic {encoded}"}
)

print(response.status_code)
print(response.json())