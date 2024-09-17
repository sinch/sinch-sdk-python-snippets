import requests

SERVICE_PLAN_ID = ""
API_TOKEN = ""
SINCH_NUMBER = ""
TO_NUMBER = ""
URL = "https://us.sms.api.sinch.com/xms/v1/" + SERVICE_PLAN_ID + "/batches"

payload = {
    "from": SINCH_NUMBER,
    "to": [
        TO_NUMBER
    ],
    "body": "Hello how are you"
}

response = requests.post(
    URL,
    json=payload,
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API_TOKEN
    }
)

data = response.json()
print(data)
