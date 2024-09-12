response = sinch_client.voice.callouts.text_to_speech(
    destination={
        "type": "number",
        "endpoint": "YOUR_phone_number"
    },
    text="Hello, this is a call from Sinch. Congratulations! You made your first call.")

print(response)
