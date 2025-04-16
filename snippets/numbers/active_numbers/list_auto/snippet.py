from sinch import SinchClient

sinch_client = SinchClient(
    project_id="YOUR_PROJECT_ID",
    key_id="KEY_ID",
    key_secret="KEY_SECRET"
)

active_numbers = sinch_client.numbers.list(
   region_code="US",
   number_type="LOCAL"
)

print("List of numbers printed one by one:\n")
for number in active_numbers.iterator():
    print(number)
