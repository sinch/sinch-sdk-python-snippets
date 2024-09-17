import requests

PROJECT_ID = "YOUR_PROJECT_ID"
PHONE_NUMBER = "YOUR_PHONE_NUMBER"
URL = "https://numbers.api.sinch.com/v1/projects/" + PROJECT_ID + "/availableNumbers/" + PHONE_NUMBER + ":rent"

payload = {
    "smsConfiguration": {
        "servicePlanId": "YOUR_servicePlanId",
        "scheduledProvisioning": {
            "status": "WAITING",
            "errorCodes": [
                "INTERNAL_ERROR"
            ]
        },
        "campaignId": "YOUR_10DLC_campaignId"
    },
    "voiceConfiguration": {
        "appId": "YOUR_appId",
        "scheduledProvisioning": {
            "status": "WAITING"
        }
    }
}

response = requests.post(
    URL,
    json=payload,
    auth=('YOUR_USERNAME', 'YOUR_PASSWORD')
)

data = response.json()
print(data)
