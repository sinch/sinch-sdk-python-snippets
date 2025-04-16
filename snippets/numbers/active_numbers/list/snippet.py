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

page_counter = 1
while True:
    print(f"Page {page_counter} List of Numbers: {active_numbers}")

    if not active_numbers.has_next_page:
        break

    active_numbers = active_numbers.next_page()
    page_counter += 1
