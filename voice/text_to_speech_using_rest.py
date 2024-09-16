import requests

KEY = ""
SECRET = ""
FROM_NUMBER = ""
TO = ""
LOCALE = ""
URL = "https://calling.api.sinch.com/calling/v1/callouts"

payload = {
    "method": "ttsCallout",
    "ttsCallout": {
        "cli": FROM_NUMBER,
        "destination": {
            "type": "number",
            "endpoint": TO
        },
        "locale": LOCALE,
        "text": "Hello, this is a call from Sinch. Congratulations! You made your first call."
    }
}

response = requests.post(
    URL,
    json=payload,
    headers={"Content-Type": "application/json"},
    auth=(KEY, SECRET)
)

data = response.json()
print(data)
