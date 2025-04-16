from sinch import SinchClient

sinch_client = SinchClient(
    project_id="YOUR_PROJECT_ID",
    key_id="KEY_ID",
    key_secret="KEY_SECRET"
)

available_numbers = sinch_client.numbers.search_for_available_numbers(
    region_code="AR",
    number_type="LOCAL"
)

print("Available numbers to rent:\n")
for number in available_numbers.iterator():
    print(number)
