from sinch import SinchClient

sinch_client = SinchClient(
    project_id="YOUR_PROJECT_ID",
    key_id="KEY_ID",
    key_secret="KEY_SECRET"
)

hmac_secret = "NEW_HMAC_SECRET"
response = sinch_client.numbers.callback_configuration.update(
    hmac_secret=hmac_secret
)

print("Updated callback configuration:\n", response)
