from sinch import SinchClient

sinch_client = SinchClient(
    key_id="YOUR_key_id",
    key_secret="YOUR_key_secret",
    project_id="YOUR_project_id"
)

available_numbers_response = sinch_client.numbers.available.list(
    region_code="YOUR_region_code",
    number_type="YOUR_number_type"
)

print(available_numbers_response)
