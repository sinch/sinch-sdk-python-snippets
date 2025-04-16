from sinch import SinchClient

sinch_client = SinchClient(
    project_id="YOUR_PROJECT_ID",
    key_id="KEY_ID",
    key_secret="KEY_SECRET"
)

phone_number = "PHONE_NUMBER"
response = sinch_client.numbers.check_availability(
    phone_number=phone_number
)

print("Released Number:\n", response)
