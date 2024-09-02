import requests

project_id = "YOUR_projectId"
phone_number = "YOUR_phoneNumber"
url = "https://numbers.api.sinch.com/v1/projects/" + project_id + "/availableNumbers/" + phone_number + ":rent"

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

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers, auth=('YOUR_username','YOUR_password'))

data = response.json()
print(data)
