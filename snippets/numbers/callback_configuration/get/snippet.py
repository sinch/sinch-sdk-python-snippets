from sinch import SinchClient

sinch_client = SinchClient(
    project_id="YOUR_PROJECT_ID",
    key_id="KEY_ID",
    key_secret="KEY_SECRET"
)

response = sinch_client.numbers.callback_configuration.get()

print("Callback Configuration:\n", response)
