from sinch import SinchClient

sinch_client = SinchClient(
    project_id="YOUR_PROJECT_ID",
    key_id="KEY_ID",
    key_secret="KEY_SECRET"
)

phone_number = "PHONE_NUMBER_TO_BE_RELEASED"
released_number = sinch_client.numbers.release(
    phone_number=phone_number
)

print("Released Number:", released_number)
