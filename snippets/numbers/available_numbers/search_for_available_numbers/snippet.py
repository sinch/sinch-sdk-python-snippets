import os
from dotenv import load_dotenv
from sinch import SinchClient

load_dotenv()

sinch_client = SinchClient(
    project_id=os.environ["PROJECT_ID"],
    key_id=os.environ["KEY_ID"],
    key_secret=os.environ["KEY_SECRET"]
)

available_numbers = sinch_client.numbers.search_for_available_numbers(
    region_code="AR",
    number_type="LOCAL"
)

print("Available numbers to rent:\n")
for number in available_numbers.iterator():
    print(number)
