from sinch import SinchClient

sinch_client = SinchClient(
    project_id="YOUR_PROJECT_ID",
    key_id="KEY_ID",
    key_secret="KEY_SECRET"
)

phone_number = "YOUR_RENTED_PHONE_NUMBER"
response = sinch_client.numbers.get(phone_number=phone_number)

print(f"Rented number details:\n{response}")
