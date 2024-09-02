import requests

service_plan_id = ""
api_token = ""
sinch_number = ""
to_number = ""
url = "https://us.sms.api.sinch.com/xms/v1/" + service_plan_id + "/batches"

payload = {
  "from": sinch_number,
  "to": [
    to_number
  ],
  "body": "Hello how are you"
}

headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer " + api_token
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)
