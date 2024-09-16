import requests

PROJECT_ID = "YOUR_PROJECT_ID"
URL = "https://numbers.api.sinch.com/v1/projects/" + PROJECT_ID + "/availableNumbers"


response = requests.get(
    URL,
    params={
        "regionCode": "US",
        "type": "LOCAL"
    },
    auth=('YOUR_USERNAME', 'YOUR_PASSWORD')
)

data = response.json()
print(data)
