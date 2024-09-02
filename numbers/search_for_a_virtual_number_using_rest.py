import requests

project_id = "YOUR_projectId"
url = "https://numbers.api.sinch.com/v1/projects/" + project_id + "/availableNumbers"

query = {
  "regionCode": "US",
  "type": "LOCAL"
}
response = requests.get(url, params=query, auth=('YOUR_username', 'YOUR_password'))

data = response.json()
print(data)
